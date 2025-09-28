import Head from 'next/head';
import { useState } from 'react';
import EmissionCalculator from '../components/EmissionCalculator';
import EmailSubscription from '../components/EmailSubscription';
import { Toaster } from 'react-hot-toast';

export default function Home() {
  const [userEmail, setUserEmail] = useState<string>('');

  return (
    <>
      <Head>
        <title>Carbon Footprint Tracker Lite</title>
        <meta name="description" content="Track and reduce your carbon footprint with our easy-to-use calculator" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <Toaster position="top-right" />

      <div className="min-h-screen bg-gradient-to-br from-green-50 to-blue-50">
        {/* Header */}
        <header className="bg-white shadow-sm">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
            <div className="flex items-center justify-between">
              <h1 className="text-2xl font-bold text-gray-900">
                🌱 Carbon Footprint Tracker Lite
              </h1>
              <nav className="hidden md:flex space-x-8">
                <a href="#calculator" className="text-gray-600 hover:text-gray-900">Calculator</a>
                <a href="#subscribe" className="text-gray-600 hover:text-gray-900">Subscribe</a>
                <a href="#about" className="text-gray-600 hover:text-gray-900">About</a>
              </nav>
            </div>
          </div>
        </header>

        {/* Hero Section */}
        <section className="py-16 px-4 sm:px-6 lg:px-8">
          <div className="max-w-4xl mx-auto text-center">
            <h2 className="text-4xl font-bold text-gray-900 mb-6">
              Take Control of Your Carbon Footprint
            </h2>
            <p className="text-xl text-gray-600 mb-8">
              Calculate the environmental impact of your daily activities and get personalized tips to reduce your carbon emissions.
            </p>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
              <div className="text-center">
                <div className="text-4xl mb-3">🚗</div>
                <h3 className="text-lg font-semibold mb-2">Transportation</h3>
                <p className="text-gray-600">Track emissions from cars, buses, flights, and more</p>
              </div>
              <div className="text-center">
                <div className="text-4xl mb-3">⚡</div>
                <h3 className="text-lg font-semibold mb-2">Energy Usage</h3>
                <p className="text-gray-600">Monitor your electricity and heating consumption</p>
              </div>
              <div className="text-center">
                <div className="text-4xl mb-3">🍽️</div>
                <h3 className="text-lg font-semibold mb-2">Food Choices</h3>
                <p className="text-gray-600">Understand the impact of your dietary decisions</p>
              </div>
            </div>
          </div>
        </section>

        {/* Calculator Section */}
        <section id="calculator" className="py-16 px-4 sm:px-6 lg:px-8 bg-white">
          <div className="max-w-4xl mx-auto">
            <EmissionCalculator userEmail={userEmail} />
          </div>
        </section>

        {/* Email Subscription Section */}
        <section id="subscribe" className="py-16 px-4 sm:px-6 lg:px-8">
          <div className="max-w-4xl mx-auto">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold text-gray-900 mb-4">
                Stay Informed & Make a Difference
              </h2>
              <p className="text-lg text-gray-600">
                Get weekly tips and insights delivered to your inbox
              </p>
            </div>
            <EmailSubscription />
          </div>
        </section>

        {/* About Section */}
        <section id="about" className="py-16 px-4 sm:px-6 lg:px-8 bg-white">
          <div className="max-w-4xl mx-auto">
            <div className="text-center">
              <h2 className="text-3xl font-bold text-gray-900 mb-8">
                About Carbon Footprint Tracker
              </h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div className="card">
                  <h3 className="text-xl font-semibold mb-4">🎯 Our Mission</h3>
                  <p className="text-gray-600">
                    Empower individuals to make informed decisions about their environmental impact through easy-to-use tools and actionable insights.
                  </p>
                </div>
                <div className="card">
                  <h3 className="text-xl font-semibold mb-4">📊 Accurate Data</h3>
                  <p className="text-gray-600">
                    Our calculations are based on scientific research and publicly available emission factors from reputable environmental organizations.
                  </p>
                </div>
                <div className="card">
                  <h3 className="text-xl font-semibold mb-4">🌍 Real Impact</h3>
                  <p className="text-gray-600">
                    Small changes in daily habits can lead to significant reductions in carbon emissions. Every action counts towards a sustainable future.
                  </p>
                </div>
                <div className="card">
                  <h3 className="text-xl font-semibold mb-4">🤝 Community</h3>
                  <p className="text-gray-600">
                    Join thousands of users who are actively working to reduce their carbon footprint and create positive environmental change.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Footer */}
        <footer className="bg-gray-800 text-white py-8">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center">
              <h3 className="text-lg font-semibold mb-2">Carbon Footprint Tracker Lite</h3>
              <p className="text-gray-400 mb-4">
                Making sustainability accessible to everyone
              </p>
              <p className="text-sm text-gray-500">
                © 2025 Carbon Footprint Tracker. Built with ❤️ for the planet.
              </p>
            </div>
          </div>
        </footer>
      </div>
    </>
  );
}