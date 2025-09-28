import { useState, useEffect } from 'react';
import { emissionAPI } from '../lib/api';

interface Activity {
  name: string;
  unit: string;
  description: string;
}

interface ActivityData {
  [category: string]: {
    [key: string]: Activity;
  };
}

interface EmissionResult {
  activity_type: string;
  quantity: number;
  co2_emissions: number;
  unit: string;
}

interface EmissionCalculatorProps {
  userEmail?: string;
}

const EmissionCalculator = ({ userEmail }: EmissionCalculatorProps) => {
  const [activities, setActivities] = useState<ActivityData>({});
  const [selectedCategory, setSelectedCategory] = useState<string>('');
  const [selectedActivity, setSelectedActivity] = useState<string>('');
  const [quantity, setQuantity] = useState<string>('');
  const [result, setResult] = useState<EmissionResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string>('');

  useEffect(() => {
    fetchActivities();
  }, []);

  const fetchActivities = async () => {
    try {
      const response = await emissionAPI.getActivities();
      setActivities(response.data);
      
      // Set default category
      const firstCategory = Object.keys(response.data)[0];
      if (firstCategory) {
        setSelectedCategory(firstCategory);
        const firstActivity = Object.keys(response.data[firstCategory])[0];
        if (firstActivity) {
          setSelectedActivity(firstActivity);
        }
      }
    } catch (err) {
      setError('Failed to load activities');
      console.error('Error fetching activities:', err);
    }
  };

  const handleCalculate = async () => {
    if (!selectedActivity || !quantity) {
      setError('Please select an activity and enter a quantity');
      return;
    }

    const numQuantity = parseFloat(quantity);
    if (isNaN(numQuantity) || numQuantity <= 0) {
      setError('Please enter a valid positive number');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const response = await emissionAPI.calculateEmissions({
        activity_type: selectedActivity,
        quantity: numQuantity,
        user_email: userEmail,
      });

      setResult(response.data);
    } catch (err) {
      setError('Failed to calculate emissions. Please try again.');
      console.error('Error calculating emissions:', err);
    } finally {
      setLoading(false);
    }
  };

  const categoryActivities = selectedCategory ? activities[selectedCategory] || {} : {};
  const selectedActivityData = categoryActivities[selectedActivity];

  return (
    <div className="card max-w-2xl mx-auto">
      <h2 className="text-2xl font-bold text-gray-800 mb-6 text-center">
        🌍 Carbon Emission Calculator
      </h2>

      {/* Category Selection */}
      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Activity Category
        </label>
        <div className="relative">
          <select
            value={selectedCategory}
            onChange={(e) => {
              setSelectedCategory(e.target.value);
              const firstActivity = Object.keys(activities[e.target.value] || {})[0];
              setSelectedActivity(firstActivity || '');
            }}
            className="input-field w-full appearance-none pr-10"
          >
            {Object.keys(activities).map((category) => (
              <option key={category} value={category}>
                {category.charAt(0).toUpperCase() + category.slice(1)}
              </option>
            ))}
          </select>
          <div className="absolute right-3 top-3 text-gray-400 pointer-events-none">▼</div>
        </div>
      </div>

      {/* Activity Selection */}
      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Specific Activity
        </label>
        <div className="relative">
          <select
            value={selectedActivity}
            onChange={(e) => setSelectedActivity(e.target.value)}
            className="input-field w-full appearance-none pr-10"
          >
            {Object.entries(categoryActivities).map(([key, activity]) => (
              <option key={key} value={key}>
                {(activity as Activity).name}
              </option>
            ))}
          </select>
          <div className="absolute right-3 top-3 text-gray-400 pointer-events-none">▼</div>
        </div>
        {selectedActivityData && (
          <p className="text-sm text-gray-600 mt-1">
            {selectedActivityData.description}
          </p>
        )}
      </div>

      {/* Quantity Input */}
      <div className="mb-6">
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Quantity
          {selectedActivityData && (
            <span className="text-gray-500 ml-1">
              ({selectedActivityData.unit.split('/')[1] || 'units'})
            </span>
          )}
        </label>
        <input
          type="number"
          value={quantity}
          onChange={(e) => setQuantity(e.target.value)}
          placeholder="Enter quantity"
          className="input-field w-full"
          min="0"
          step="any"
        />
      </div>

      {/* Calculate Button */}
      <button
        onClick={handleCalculate}
        disabled={loading || !selectedActivity || !quantity}
        className="btn-primary w-full mb-4 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        {loading ? 'Calculating...' : 'Calculate CO₂ Emissions'}
      </button>

      {/* Error Message */}
      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      {/* Result Display */}
      {result && (
        <div className="bg-primary-50 border border-primary-200 rounded-lg p-6">
          <h3 className="text-lg font-semibold text-primary-800 mb-2">
            💨 Emission Result
          </h3>
          <div className="space-y-2">
            <p className="text-gray-700">
              <span className="font-medium">Activity:</span> {categoryActivities[result.activity_type]?.name}
            </p>
            <p className="text-gray-700">
              <span className="font-medium">Quantity:</span> {result.quantity} {result.unit.split('/')[1]}
            </p>
            <p className="text-2xl font-bold text-primary-700">
              🌫️ {result.co2_emissions} kg CO₂
            </p>
          </div>
          
          {/* Environmental Context */}
          <div className="mt-4 p-4 bg-blue-50 rounded-lg">
            <p className="text-sm text-blue-800">
              💡 <strong>Context:</strong> {getEmissionContext(result.co2_emissions)}
            </p>
          </div>
        </div>
      )}
    </div>
  );
};

const getEmissionContext = (emissions: number): string => {
  if (emissions < 1) {
    return "Great choice! This is a low-carbon activity.";
  } else if (emissions < 5) {
    return "This produces moderate emissions. Consider alternatives when possible.";
  } else if (emissions < 20) {
    return "This activity has significant carbon impact. Look for greener alternatives.";
  } else {
    return "High carbon impact! Consider offsetting or finding sustainable alternatives.";
  }
};

export default EmissionCalculator;