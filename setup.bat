@echo off
REM Carbon Footprint Tracker - Development Setup Script for Windows

echo 🌍 Setting up Carbon Footprint Tracker...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed. Please install Python 3.9+ first.
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Node.js is not installed. Please install Node.js 18+ first.
    exit /b 1
)

echo ✅ Prerequisites check passed

REM Setup Backend
echo 🐍 Setting up Backend...
cd backend

REM Create virtual environment
python -m venv venv
call venv\Scripts\activate.bat

REM Install Python dependencies
pip install -r requirements.txt

REM Copy environment file
if not exist .env (
    copy .env.example .env
    echo 📝 Created .env file from .env.example - please update with your settings
)

cd ..

REM Setup Frontend
echo ⚛️  Setting up Frontend...
cd frontend

REM Install Node.js dependencies
npm install

REM Create environment file
if not exist .env.local (
    echo NEXT_PUBLIC_API_URL=http://localhost:8000 > .env.local
    echo 📝 Created .env.local file
)

cd ..

echo.
echo 🎉 Setup complete!
echo.
echo To start the application:
echo 1. Backend:  cd backend && venv\Scripts\activate && uvicorn app.main:app --reload
echo 2. Frontend: cd frontend && npm run dev
echo.
echo Then visit:
echo - Frontend: http://localhost:3000
echo - API Docs: http://localhost:8000/docs

pause