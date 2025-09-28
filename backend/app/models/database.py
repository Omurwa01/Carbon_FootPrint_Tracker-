from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    is_subscribed = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Activity(Base):
    __tablename__ = "activities"
    
    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String(255), index=True)
    activity_type = Column(String(100), index=True)
    quantity = Column(Float)
    co2_emissions = Column(Float)  # kg of CO2
    created_at = Column(DateTime(timezone=True), server_default=func.now())