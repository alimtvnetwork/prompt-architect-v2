param (
    [string]$TargetDir = ".lovable/prompts",
    [string]$Version = "main"
)

Write-Host "Installing Prompt Architect v$Version into $TargetDir..."

if (Test-Path $TargetDir) {
    if (Test-Path "$TargetDir\prompt-version.json") {
        $oldVersion = (Get-Content "$TargetDir\prompt-version.json" | ConvertFrom-Json).version
        Write-Host "Removing old version: $oldVersion"
    }
    Remove-Item -Path "$TargetDir\*" -Recurse -Force -ErrorAction SilentlyContinue
} else {
    New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
}

$tempDir = [System.IO.Path]::GetTempPath() + [guid]::NewGuid().ToString()

try {
    Write-Host "Cloning version $Version..."
    git clone -q --depth 1 --branch $Version https://github.com/alimtvnetwork/prompt-architect-v2.git $tempDir
    
    Write-Host "Copying prompts..."
    Copy-Item -Path "$tempDir\01-general-prompts\*" -Destination $TargetDir -Recurse -Force
    
    $versionInfo = @{
        version = $Version
        installed_at = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
    }
    $versionInfo | ConvertTo-Json | Set-Content "$TargetDir\prompt-version.json"
    
    Write-Host "Successfully installed Prompt Architect $Version!"
} finally {
    if (Test-Path $tempDir) {
        Remove-Item -Path $tempDir -Recurse -Force -ErrorAction SilentlyContinue
    }
}
