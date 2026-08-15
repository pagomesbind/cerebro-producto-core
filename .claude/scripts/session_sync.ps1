<#
.SYNOPSIS
  SessionStart hook: snapshot diario del repo personal + pull/espejo de CEREBRO_CORE.

  Determinista, sin LLM. Throttle de una corrida por dia via archivo de marca.
  Tolerante a que CEREBRO_CORE todavia no exista (identidad.local.md sin
  ruta_clon_core, o carpeta no encontrada) -- en ese caso solo hace el snapshot
  personal y saltea el resto en silencio.

  Cualquier error se loguea a .claude/scripts/session_sync.log y NUNCA rompe el
  arranque de la sesion (siempre exit 0).
#>

$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot  = Split-Path -Parent (Split-Path -Parent $scriptDir)   # .claude/scripts -> .claude -> repo root
$logFile   = Join-Path $scriptDir 'session_sync.log'
$marker    = Join-Path $repoRoot 'wiki\1_proyectos\logs_sync\.ultimo_pull'

function Write-Log {
    param([string]$Message)
    $line = "[{0:yyyy-MM-dd HH:mm:ss}] {1}" -f (Get-Date), $Message
    try { Add-Content -Path $logFile -Value $line -Encoding utf8 } catch {}
}

function Test-ShouldRun {
    if (-not (Test-Path $marker)) { return $true }
    try {
        $last = Get-Content -Path $marker -Raw -ErrorAction Stop | ForEach-Object { $_.Trim() }
        $lastDate = [datetime]::Parse($last)
        return ((Get-Date) - $lastDate).TotalHours -ge 24
    } catch {
        return $true
    }
}

function Update-Marker {
    try {
        $dir = Split-Path -Parent $marker
        if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
        (Get-Date).ToString('o') | Set-Content -Path $marker -Encoding utf8
    } catch {
        Write-Log "No se pudo actualizar el marker: $_"
    }
}

function Get-RutaClonCore {
    $identidad = Join-Path $repoRoot 'identidad.local.md'
    if (-not (Test-Path $identidad)) { return $null }
    try {
        $content = Get-Content -Path $identidad -Raw -Encoding utf8
        if ($content -match '(?m)^ruta_clon_core:\s*(.*)$') {
            $val = $Matches[1].Trim()
            # Quitar comentario YAML inline (todo desde un '#' que no esta dentro de comillas)
            if ($val -match "^(['`"]?)([^#]*)\1\s*#") {
                $val = $Matches[2].Trim()
            } elseif ($val.StartsWith('#')) {
                $val = ''
            }
            $val = $val.Trim() -replace '^["'']|["'']$', ''
            if ([string]::IsNullOrWhiteSpace($val)) { return $null }
            return $val
        }
    } catch {
        Write-Log "No se pudo leer identidad.local.md: $_"
    }
    return $null
}

function Invoke-SnapshotPersonal {
    Write-Log "Snapshot personal: arrancando en $repoRoot"
    try {
        Push-Location $repoRoot
        git add -A 2>&1 | Out-Null
        $staged = git diff --cached --name-only 2>&1
        if ($staged -and $staged.Trim().Length -gt 0) {
            $msg = "Cerebro -- snapshot {0:yyyy-MM-dd}" -f (Get-Date)
            git commit -m $msg 2>&1 | Out-Null
            $pushOut = git push origin main 2>&1
            Write-Log "Snapshot commiteado y pusheado: $msg"
        } else {
            Write-Log "Snapshot: sin cambios, nada para commitear."
        }
    } catch {
        Write-Log "Error en snapshot personal (no bloqueante): $_"
    } finally {
        Pop-Location
    }
}

function Invoke-PullYEspejoCore {
    param([string]$CoreDir)

    if ([string]::IsNullOrWhiteSpace($CoreDir) -or -not (Test-Path $CoreDir)) {
        Write-Log "CEREBRO_CORE todavia no existe o ruta invalida ('$CoreDir') -- se saltea pull/espejo."
        return
    }

    $manifiestosDir = Join-Path $CoreDir 'manifiestos'
    $manifiestosAntes = @()
    if (Test-Path $manifiestosDir) {
        $manifiestosAntes = Get-ChildItem -Path $manifiestosDir -File -ErrorAction SilentlyContinue |
            Select-Object -ExpandProperty Name
    }

    try {
        Push-Location $CoreDir
        $pullOut = git pull --ff-only 2>&1
        Write-Log "git pull en CEREBRO_CORE: $pullOut"
    } catch {
        Write-Log "Error haciendo git pull en CEREBRO_CORE (no bloqueante): $_"
        Pop-Location
        return
    } finally {
        if ((Get-Location).Path -ne $repoRoot) { Pop-Location -ErrorAction SilentlyContinue }
    }

    # Espejo: wiki/2_areas, wiki/3_recursos, .claude/skills, .claude/scripts
    $mirrors = @(
        @{ Src = (Join-Path $CoreDir 'wiki\2_areas');    Dst = (Join-Path $repoRoot 'wiki\2_areas') },
        @{ Src = (Join-Path $CoreDir 'wiki\3_recursos'); Dst = (Join-Path $repoRoot 'wiki\3_recursos') },
        @{ Src = (Join-Path $CoreDir '.claude\skills');  Dst = (Join-Path $repoRoot '.claude\skills') },
        @{ Src = (Join-Path $CoreDir '.claude\scripts'); Dst = (Join-Path $repoRoot '.claude\scripts') }
    )
    foreach ($m in $mirrors) {
        if (Test-Path $m.Src) {
            try {
                robocopy $m.Src $m.Dst /MIR /NFL /NDL /NJH /NJS /NC /NS 1>$null 2>&1
                Write-Log "Espejo OK: $($m.Src) -> $($m.Dst)"
            } catch {
                Write-Log "Error espejando $($m.Src): $_"
            }
        } else {
            Write-Log "Fuente de espejo no encontrada, se saltea: $($m.Src)"
        }
    }

    # Archivos sueltos (robocopy con lista de archivos)
    $singleFiles = @(
        @{ SrcDir = $CoreDir;                     Dst = $repoRoot;                    Name = 'CLAUDE.md' },
        @{ SrcDir = (Join-Path $CoreDir '.claude'); Dst = (Join-Path $repoRoot '.claude'); Name = 'settings.json' }
    )
    foreach ($f in $singleFiles) {
        $srcFile = Join-Path $f.SrcDir $f.Name
        if (Test-Path $srcFile) {
            try {
                robocopy $f.SrcDir $f.Dst $f.Name /NFL /NDL /NJH /NJS /NC /NS 1>$null 2>&1
                Write-Log "Espejo OK: $srcFile -> $($f.Dst)\$($f.Name)"
            } catch {
                Write-Log "Error espejando $srcFile : $_"
            }
        }
    }

    # Aviso de manifiestos nuevos
    if (Test-Path $manifiestosDir) {
        $manifiestosAhora = Get-ChildItem -Path $manifiestosDir -File -ErrorAction SilentlyContinue |
            Select-Object -ExpandProperty Name
        $nuevos = $manifiestosAhora | Where-Object { $manifiestosAntes -notcontains $_ }
        if ($nuevos -and $nuevos.Count -gt 0) {
            Write-Output "Cerebro: hay $($nuevos.Count) manifiesto(s) de merge nuevo(s) en CEREBRO_CORE -- corre /context_pull para verlos."
            Write-Log "Manifiestos nuevos detectados: $($nuevos -join ', ')"
        }
    }
}

# --- Main ---
try {
    if (-not (Test-ShouldRun)) {
        exit 0
    }

    Invoke-SnapshotPersonal

    $coreDir = Get-RutaClonCore
    Invoke-PullYEspejoCore -CoreDir $coreDir

    Update-Marker
} catch {
    Write-Log "Error inesperado en session_sync.ps1 (no bloqueante): $_"
}

exit 0
