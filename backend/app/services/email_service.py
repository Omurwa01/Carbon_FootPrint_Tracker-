import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List
import random

class EmailService:
    def __init__(self):
        self.sendgrid_api_key = os.getenv("SENDGRID_API_KEY")
        self.from_email = os.getenv("FROM_EMAIL", "noreply@carbontracker.com")
        
        # Weekly carbon reduction tips
        self.weekly_tips = [
            "🚗 Try carpooling or using public transport once this week to reduce your transport emissions by up to 45%.",
            "💡 Switch to LED bulbs - they use 75% less energy and last 25 times longer than incandescent bulbs.",
            "🥗 Try having one plant-based meal today. Beef production creates 27kg of CO₂ per kg, while vegetables create only 2kg.",
            "♻️ Recycle properly this week. Recycling aluminum cans saves 95% of the energy needed to make new ones.",
            "🚿 Take shorter showers. A 4-minute shower uses about 40 gallons less water than an 8-minute shower.",
            "🌡️ Lower your thermostat by 2°F in winter and raise it by 2°F in summer to save energy without sacrificing comfort.",
            "🔌 Unplug electronics when not in use. Many devices consume energy even when turned off.",
            "🚴 Walk or bike for short trips under 2 miles. It's good for you and produces zero emissions!",
            "📱 Buy only what you need. The production of new items has a significant carbon footprint.",
            "🌱 Start composting food scraps. It reduces methane emissions from landfills and creates nutrient-rich soil."
        ]
    
    def get_random_tip(self) -> str:
        """Get a random carbon reduction tip"""
        return random.choice(self.weekly_tips)
    
    def send_weekly_tip(self, email: str) -> bool:
        """Send a weekly carbon reduction tip email"""
        try:
            # For demo purposes, we'll just return True
            # In production, you'd integrate with SendGrid, Mailgun, etc.
            tip = self.get_random_tip()
            
            # Mock email sending logic
            print(f"Sending email to {email}: {tip}")
            
            # Here you would implement actual email sending:
            # - SendGrid API
            # - SMTP
            # - Other email service
            
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False
    
    def send_welcome_email(self, email: str) -> bool:
        """Send welcome email to new subscribers"""
        try:
            welcome_message = """
            Welcome to Carbon Footprint Tracker! 🌍
            
            Thank you for taking the first step towards a more sustainable lifestyle.
            
            You'll receive weekly tips to help reduce your carbon footprint.
            Every small action counts towards a healthier planet!
            
            Best regards,
            The Carbon Tracker Team
            """
            
            print(f"Sending welcome email to {email}")
            return True
        except Exception as e:
            print(f"Failed to send welcome email: {e}")
            return False

# Global instance
email_service = EmailService()