#!/usr/bin/env python3
"""
Database connection test script for MySQL
"""
import os
import sys
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_database_connection():
    """Test the database connection"""
    try:
        # Get database URL
        database_url = os.getenv("DATABASE_URL")
        print(f"Testing connection to: {database_url.replace(':1234@', ':****@')}")
        
        # Create engine
        engine = create_engine(database_url)
        
        # Test connection
        with engine.connect() as connection:
            # Test basic connection
            result = connection.execute(text("SELECT 1 as test"))
            test_value = result.scalar()
            
            if test_value == 1:
                print("✅ Database connection successful!")
                
                # Check if database exists and has proper character set
                result = connection.execute(text("SELECT DATABASE() as db_name"))
                db_name = result.scalar()
                print(f"✅ Connected to database: {db_name}")
                
                # Check MySQL version
                result = connection.execute(text("SELECT VERSION() as version"))
                version = result.scalar()
                print(f"✅ MySQL version: {version}")
                
                return True
            else:
                print("❌ Database connection test failed")
                return False
                
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        
        # Provide troubleshooting tips
        print("\n🔧 Troubleshooting tips:")
        print("1. Make sure MySQL server is running")
        print("2. Verify the database 'SDG_PROJECT' exists")
        print("3. Check that user 'root' has access to the database")
        print("4. Confirm the password is correct")
        print("5. Ensure MySQL is listening on port 3306")
        
        return False

if __name__ == "__main__":
    success = test_database_connection()
    sys.exit(0 if success else 1)