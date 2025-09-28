#!/bin/bash

# Quick start script for development

echo "🚀 Starting Carbon Footprint Tracker..."

# Check if we're in the right directory
if [ ! -f "README.md" ]; then
    echo "❌ Please run this script from the project root directory"
    exit 1
fi

# Function to start backend
start_backend() {
    echo "🐍 Starting Backend..."
    cd backend
    
    # Activate virtual environment if it exists
    if [ -d "venv" ]; then
        source venv/bin/activate  # On Windows use: venv\Scripts\activate
    fi
    
    # Install dependencies if not installed
    if [ ! -d "venv" ]; then
        echo "Setting up virtual environment..."
        python -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
    fi
    
    # Start the server
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &
    BACKEND_PID=$!
    
    cd ..
}

# Function to start frontend
start_frontend() {
    echo "⚛️  Starting Frontend..."
    cd frontend
    
    # Install dependencies if not installed
    if [ ! -d "node_modules" ]; then
        echo "Installing npm dependencies..."
        npm install
    fi
    
    # Start the development server
    npm run dev &
    FRONTEND_PID=$!
    
    cd ..
}

# Start both services
start_backend
sleep 3  # Give backend time to start
start_frontend

echo ""
echo "✅ Services starting..."
echo "🔗 Frontend: http://localhost:3000"
echo "📚 API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop all services"

# Handle cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Stopping services..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    echo "✅ All services stopped"
    exit 0
}

trap cleanup INT TERM

# Wait for user to stop
wait