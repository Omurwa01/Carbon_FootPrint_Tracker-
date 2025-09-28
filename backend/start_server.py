import os
import sys
import subprocess

# Change to the backend directory
backend_dir = r"E:\oficial_SDG_PROJECT\backend"
os.chdir(backend_dir)

print(f"Changed directory to: {os.getcwd()}")
print("Starting FastAPI server...")

# Start uvicorn
cmd = [sys.executable, "-m", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
subprocess.run(cmd)