#!/bin/bash

# Carbon Footprint Tracker - Development Setup Script

echo "🌍 Setting up Carbon Footprint Tracker..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.9+ first."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 18+ first."
    exit 1
fi

echo "✅ Prerequisites check passed"

# Setup Backend
echo "🐍 Setting up Backend..."
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Copy environment file
if [ ! -f .env ]; then
    cp .env.example .env
    echo "📝 Created .env file from .env.example - please update with your settings"
fi

cd ..

# Setup Frontend
echo "⚛️  Setting up Frontend..."
cd frontend

# Install Node.js dependencies
npm install

# Create environment file
if [ ! -f .env.local ]; then
    echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
    echo "📝 Created .env.local file"
fi

cd ..

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To start the application:"
echo "1. Backend:  cd backend && source venv/bin/activate && uvicorn app.main:app --reload"
echo "2. Frontend: cd frontend && npm run dev"
echo ""
echo "Then visit:"
echo "- Frontend: http://localhost:3000"
echo "- API Docs: http://localhost:8000/docs"