#!/usr/bin/env python3
"""
Create database script for MySQL
"""
import pymysql
from sqlalchemy import create_engine, text

def create_database():
    """Create the SDG_PROJECT database if it doesn't exist"""
    try:
        # Connect to MySQL server without specifying database
        connection_url = "mysql+pymysql://root:1234@127.0.0.1:3306/"
        engine = create_engine(connection_url)
        
        with engine.connect() as connection:
            # Set autocommit to True for CREATE DATABASE
            connection.execute(text("SET autocommit = 1"))
            
            # Create database if it doesn't exist
            connection.execute(text("CREATE DATABASE IF NOT EXISTS `SDG_PROJECT` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"))
            print("✅ Database 'SDG_PROJECT' created successfully!")
            
            # Verify database was created
            result = connection.execute(text("SHOW DATABASES LIKE 'SDG_PROJECT'"))
            if result.fetchone():
                print("✅ Database verified to exist")
                return True
            else:
                print("❌ Database creation verification failed")
                return False
                
    except Exception as e:
        print(f"❌ Failed to create database: {e}")
        return False

if __name__ == "__main__":
    success = create_database()
    if success:
        print("\n🎉 Database setup complete!")
        print("You can now run the FastAPI server.")
    else:
        print("\n❌ Database setup failed. Please check your MySQL server.")