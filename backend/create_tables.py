#!/usr/bin/env python3
"""
Create database tables script
"""
import os
import sys

# Add the current directory to Python path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import engine
from app.models.database import Base
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_tables():
    """Create all database tables"""
    try:
        # Create all tables
        print("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        print("✅ All tables created successfully!")
        
        # List the tables that were created
        from sqlalchemy import inspect
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        
        print(f"📋 Created tables: {', '.join(tables)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Failed to create tables: {e}")
        return False

if __name__ == "__main__":
    success = create_tables()
    if success:
        print("\n🎉 Database schema setup complete!")
        print("You can now use the API endpoints.")
    else:
        print("\n❌ Database schema setup failed.")