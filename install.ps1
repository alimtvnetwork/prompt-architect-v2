param (
    [string]$TargetDir = ".lovable/prompts",
    [string]$Version = "main"
)

Write-Host "Installing Prompt Architect v$Version into $TargetDir..."

# Try to find the root of the repo (assume it's the current directory where the script is invoked)
$RepoRoot = (Get-Item .).FullName
$VersionJsonPath = Join-Path $RepoRoot "version.json"

if (Test-Path $TargetDir) {
    Remove-Item -Path "$TargetDir\*" -Recurse -Force -ErrorAction SilentlyContinue
} else {
    New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
}

$tempDir = [System.IO.Path]::GetTempPath() + [guid]::NewGuid().ToString()

try {
    Write-Host "Cloning version $Version..."
    git clone -q --depth 1 --branch $Version https://github.com/alimtvnetwork/prompt-architect-v2.git $tempDir
    
    Write-Host "Copying prompts..."
    Copy-Item -Path "$TempDir\01-general-prompts\*" -Destination $TargetDir -Recurse -Force

    Write-Host "Copying ai-fix-scripts..." -ForegroundColor Cyan
    $AiFixScriptsTarget = Join-Path (Split-Path $TargetDir -Parent) "ai-fix-scripts"
    if (-not (Test-Path $AiFixScriptsTarget)) { New-Item -ItemType Directory -Force -Path $AiFixScriptsTarget | Out-Null }
    Copy-Item -Path "$TempDir\.lovable\ai-fix-scripts\*" -Destination $AiFixScriptsTarget -Recurse -Force -ErrorAction SilentlyContinue

    Write-Host "Copying release automation scripts..." -ForegroundColor Cyan
    $ReleaseTarget = Join-Path (Split-Path $TargetDir -Parent) "release"
    if (-not (Test-Path $ReleaseTarget)) { New-Item -ItemType Directory -Force -Path $ReleaseTarget | Out-Null }
    Copy-Item -Path "$TempDir\.lovable\release\bump_versions.py" -Destination $ReleaseTarget -Force -ErrorAction SilentlyContinue
    Copy-Item -Path "$TempDir\.lovable\release\release-method.md" -Destination $ReleaseTarget -Force -ErrorAction SilentlyContinue

    Write-Host "Copying ai-fix-scripts..." -ForegroundColor Cyan
    $AiFixScriptsTarget = Join-Path (Split-Path $TargetDir -Parent) "ai-fix-scripts"
    if (-not (Test-Path $AiFixScriptsTarget)) { New-Item -ItemType Directory -Force -Path $AiFixScriptsTarget | Out-Null }
    Copy-Item -Path "$TempDir\.lovable\ai-fix-scripts\*" -Destination $AiFixScriptsTarget -Recurse -Force -ErrorAction SilentlyContinue
    

    Write-Host "Copying .agents (Antigravity Skills & Rules)..." -ForegroundColor Cyan
    $AgentsTarget = Join-Path $RepoRoot ".agents"
    if (-not (Test-Path $AgentsTarget)) { New-Item -ItemType Directory -Force -Path $AgentsTarget | Out-Null }
    Copy-Item -Path "$TempDir\.agents\*" -Destination $AgentsTarget -Recurse -Force -ErrorAction SilentlyContinue
    
    Write-Host "Copying root agents.md..." -ForegroundColor Cyan
    Copy-Item -Path "$TempDir\agents.md" -Destination (Join-Path $RepoRoot "agents.md") -Force -ErrorAction SilentlyContinue

    # Generate list of imported files
    $importedFiles = Get-ChildItem -Path $TargetDir -Recurse -File | Select-Object -ExpandProperty FullName
    $relativeFiles = $importedFiles | ForEach-Object { $_.Replace($RepoRoot + "\", "").Replace("\", "/") }
    
    $promptData = @{
        version = $Version
        installed_at = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
        author = @{
            name = "Md. Alim Ul Karim"
            title = "Chief Software Engineer"
            url = "https://github.com/alimtvnetwork/prompt-architect-v2"
        }
        mapping = @{
            source_repository = "alimtvnetwork/prompt-architect-v2"
            source_directory = "01-general-prompts"
            target_directory = $TargetDir.Replace("\", "/")
            files_imported = $relativeFiles
        }
    }

    if (Test-Path $VersionJsonPath) {
        Write-Host "Updating $VersionJsonPath with Prompt Architect metadata..."
        $jsonContent = Get-Content $VersionJsonPath -Raw | ConvertFrom-Json
        
        # Cross-PS version compatible update
        if ($null -eq $jsonContent.promptArchitectByRiseupAsia) {
            $jsonContent | Add-Member -MemberType NoteProperty -Name "promptArchitectByRiseupAsia" -Value $promptData
        } else {
            $jsonContent.promptArchitectByRiseupAsia = $promptData
        }
        
        $jsonContent | ConvertTo-Json -Depth 10 | Set-Content $VersionJsonPath
    } else {
        Write-Host "Creating new $VersionJsonPath with Prompt Architect metadata..."
        $newJson = @{
            name = "unknown-project"
            version = "0.0.0"
            frontend = @{ version = "inherit" }
            backend = @{ version = "inherit" }
            changelog = @{ file_path = "changelog.md"; format = "## [v{version}] {date} {headline}" }
            promptArchitectByRiseupAsia = $promptData
        }
        $newJson | ConvertTo-Json -Depth 10 | Set-Content $VersionJsonPath
    }
    
    Write-Host "Successfully installed Prompt Architect $Version!"
} finally {
    if (Test-Path $tempDir) {
        Remove-Item -Path $tempDir -Recurse -Force -ErrorAction SilentlyContinue
    }
}
