import json
import os
from typing import Dict, Optional

class EmissionService:
    def __init__(self):
        self.emission_factors = self._load_emission_factors()
    
    def _load_emission_factors(self) -> Dict:
        """Load emission factors from JSON file"""
        current_dir = os.path.dirname(__file__)
        json_path = os.path.join(current_dir, "..", "emission_factors.json")
        
        with open(json_path, 'r') as file:
            return json.load(file)
    
    def calculate_emissions(self, activity_type: str, quantity: float) -> Optional[Dict]:
        """Calculate CO2 emissions for a given activity and quantity"""
        # Find the activity in the nested structure
        for category, activities in self.emission_factors.items():
            if activity_type in activities:
                factor_data = activities[activity_type]
                factor = factor_data["factor"]
                emissions = factor * quantity
                
                return {
                    "activity_type": activity_type,
                    "quantity": quantity,
                    "co2_emissions": round(emissions, 3),
                    "unit": factor_data["unit"],
                    "name": factor_data["name"],
                    "description": factor_data["description"]
                }
        
        return None
    
    def get_all_activities(self) -> Dict:
        """Get all available activities organized by category"""
        result = {}
        for category, activities in self.emission_factors.items():
            result[category] = {}
            for key, data in activities.items():
                result[category][key] = {
                    "name": data["name"],
                    "unit": data["unit"],
                    "description": data["description"]
                }
        return result
    
    def get_activity_categories(self) -> list:
        """Get list of all activity categories"""
        return list(self.emission_factors.keys())

# Global instance
emission_service = EmissionService()