import { useState, FormEvent } from 'react';
import { userAPI } from '../lib/api';
import toast from 'react-hot-toast';

const EmailSubscription = () => {
  const [email, setEmail] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    
    if (!email || !email.includes('@')) {
      toast.error('Please enter a valid email address');
      return;
    }

    setLoading(true);

    try {
      await userAPI.subscribeUser({
        email,
        is_subscribed: true,
      });

      toast.success('Successfully subscribed! You\'ll receive weekly carbon tips.');
      setEmail('');
    } catch (error: any) {
      if (error.response?.status === 400) {
        toast.error('This email is already subscribed!');
      } else {
        toast.error('Failed to subscribe. Please try again.');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card max-w-md mx-auto">
      <h3 className="text-xl font-semibold text-gray-800 mb-4 text-center">
        📧 Get Weekly Carbon Tips
      </h3>
      <p className="text-gray-600 text-center mb-6">
        Subscribe to receive personalized tips for reducing your carbon footprint
      </p>
      
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your email address"
            className="input-field w-full"
            required
          />
        </div>
        
        <button
          type="submit"
          disabled={loading}
          className="btn-primary w-full disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {loading ? 'Subscribing...' : 'Subscribe for Tips'}
        </button>
      </form>
      
      <p className="text-xs text-gray-500 text-center mt-4">
        We respect your privacy. Unsubscribe anytime.
      </p>
    </div>
  );
};

export default EmailSubscription;