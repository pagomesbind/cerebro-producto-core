<#
.SYNOPSIS
  PreToolUse hook: bloquea Edit/Write sobre las rutas espejadas de CEREBRO_CORE.

  Estas rutas son read-only en este install -- solo /context_merge las escribe,
  y solo sobre el clon del repo compartido. Ver CLAUDE.md, seccion "Regla central".
#>

$ErrorActionPreference = 'Stop'

try {
    $stdin = [Console]::In.ReadToEnd()
    $payload = $stdin | ConvertFrom-Json
} catch {
    # Si no se puede parsear el input, no bloqueamos por las dudas de romper la sesion.
    exit 0
}

$filePath = $payload.tool_input.file_path
if ([string]::IsNullOrWhiteSpace($filePath)) {
    exit 0
}

# Repo root = directorio de trabajo del hook (Claude Code lo corre desde la raiz del proyecto).
$repoRoot = (Get-Location).Path

# Normalizar a ruta absoluta y separadores consistentes.
try {
    $fullPath = [System.IO.Path]::GetFullPath($filePath)
} catch {
    $fullPath = $filePath
}
$fullPath = $fullPath -replace '/', '\'
$repoRootNorm = ($repoRoot -replace '/', '\').TrimEnd('\')

# settings.local.json nunca se bloquea (config personal, no espejada).
if ($fullPath -like "*\.claude\settings.local.json") {
    exit 0
}

$exactClaudeMd  = Join-Path $repoRootNorm 'CLAUDE.md'
$exactSettings  = Join-Path $repoRootNorm '.claude\settings.json'
$blockedExact   = @($exactClaudeMd, $exactSettings)

$prefixAreas    = (Join-Path $repoRootNorm 'wiki\2_areas') + '\'
$prefixRecursos = (Join-Path $repoRootNorm 'wiki\3_recursos') + '\'
$prefixSkills   = (Join-Path $repoRootNorm '.claude\skills') + '\'
$prefixScripts  = (Join-Path $repoRootNorm '.claude\scripts') + '\'
$blockedPrefixes = @($prefixAreas, $prefixRecursos, $prefixSkills, $prefixScripts)

$isBlocked = $false

foreach ($exact in $blockedExact) {
    if ($fullPath -ieq $exact) { $isBlocked = $true; break }
}
if (-not $isBlocked) {
    foreach ($prefix in $blockedPrefixes) {
        if ($fullPath.StartsWith($prefix, [System.StringComparison]::OrdinalIgnoreCase)) {
            $isBlocked = $true
            break
        }
    }
}

if ($isBlocked) {
    $reason = "Esta ruta es un espejo read-only de CEREBRO_CORE. Todo aporte al canon debe " +
              "capturarse como item en wiki/1_proyectos/contexto_vivo/ (ver CLAUDE.md) -- " +
              "nunca escribirse aca directo. Unica excepcion: /context_merge, corriendo sobre " +
              "el clon del repo compartido, no sobre este install."
    $output = @{
        hookSpecificOutput = @{
            hookEventName = 'PreToolUse'
            permissionDecision = 'deny'
            permissionDecisionReason = $reason
        }
        systemMessage = $reason
    }
    $output | ConvertTo-Json -Depth 5 -Compress
    exit 0
}

exit 0
