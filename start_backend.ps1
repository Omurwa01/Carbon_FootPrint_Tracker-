# Navigate to backend directory
Set-Location "E:\oficial_SDG_PROJECT\backend"

# Display current directory
Write-Host "Current directory: $(Get-Location)" -ForegroundColor Green

# Check if app module exists
if (Test-Path "app") {
    Write-Host "✅ App module found" -ForegroundColor Green
} else {
    Write-Host "❌ App module not found" -ForegroundColor Red
    exit 1
}

# Start the FastAPI server
Write-Host "🚀 Starting FastAPI server..." -ForegroundColor Cyan
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000