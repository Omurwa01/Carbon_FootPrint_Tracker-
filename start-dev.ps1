# Quick start script for Windows development

Write-Host "🚀 Starting Carbon Footprint Tracker..." -ForegroundColor Green

# Check if we're in the right directory
if (-not (Test-Path "README.md")) {
    Write-Host "❌ Please run this script from the project root directory" -ForegroundColor Red
    exit 1
}

# Start Backend
Write-Host "🐍 Starting Backend..." -ForegroundColor Yellow

# Navigate to backend directory
Push-Location backend

# Check if virtual environment exists, create if not
if (-not (Test-Path "venv")) {
    Write-Host "Setting up virtual environment..." -ForegroundColor Cyan
    python -m venv venv
    & "venv\Scripts\Activate.ps1"
    pip install -r requirements.txt
} else {
    & "venv\Scripts\Activate.ps1"
}

# Start backend in background
Start-Process -FilePath "python" -ArgumentList "-m", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000" -WindowStyle Hidden

Pop-Location

# Wait a moment for backend to start
Start-Sleep -Seconds 3

# Start Frontend
Write-Host "⚛️  Starting Frontend..." -ForegroundColor Yellow

Push-Location frontend

# Install dependencies if needed
if (-not (Test-Path "node_modules")) {
    Write-Host "Installing npm dependencies..." -ForegroundColor Cyan
    npm install
}

# Start frontend in background
Start-Process -FilePath "npm" -ArgumentList "run", "dev" -WindowStyle Hidden

Pop-Location

Write-Host ""
Write-Host "✅ Services starting..." -ForegroundColor Green
Write-Host "🔗 Frontend: http://localhost:3000" -ForegroundColor Cyan
Write-Host "📚 API Docs: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press any key to stop all services..." -ForegroundColor Yellow

# Wait for user input
$null = Read-Host

# Stop all processes
Write-Host "🛑 Stopping services..." -ForegroundColor Red
Get-Process | Where-Object {$_.ProcessName -eq "python" -or $_.ProcessName -eq "node"} | Stop-Process -Force
Write-Host "✅ All services stopped" -ForegroundColor Green