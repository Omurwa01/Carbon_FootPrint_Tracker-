# Carbon Footprint Tracker Lite 🌍

A production-ready web application for tracking and calculating carbon emissions from daily activities. Built with FastAPI (Python) backend and Next.js (React) frontend.

## 🚀 Features

- **Real-time Carbon Calculations**: Calculate CO₂ emissions for various activities (transport, energy, food, household)
- **Comprehensive Activity Database**: 25+ activities across 4 categories with realistic emission factors
- **Email Subscriptions**: Weekly carbon reduction tips via email
- **Activity History**: Track user's emission calculations over time
- **Responsive Design**: Clean, mobile-friendly UI with TailwindCSS
- **Production Ready**: Proper error handling, validation, and deployment configurations

## 📁 Project Structure

```
carbon-footprint-tracker/
├── backend/                    # FastAPI backend
│   ├── app/
│   │   ├── models/            # Database models and schemas
│   │   ├── routers/           # API route handlers
│   │   ├── services/          # Business logic services
│   │   ├── main.py           # FastAPI app configuration
│   │   ├── database.py       # Database setup
│   │   └── emission_factors.json  # Carbon emission factors
│   ├── requirements.txt       # Python dependencies
│   ├── pyproject.toml        # Poetry configuration
│   └── .env.example          # Environment variables template
├── frontend/                  # Next.js frontend
│   ├── components/           # React components
│   ├── lib/                  # API client and utilities
│   ├── pages/                # Next.js pages
│   ├── styles/               # CSS styles
│   └── package.json          # Node.js dependencies
└── README.md                 # This file
```

## 🛠️ Quick Start

### Prerequisites

- Python 3.9+
- Node.js 18+
- PostgreSQL (optional, SQLite used by default)

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Install dependencies:**
   ```bash
   # Using pip
   pip install -r requirements.txt
   
   # Or using Poetry
   poetry install
   ```

3. **Set up environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your configurations
   ```

4. **Run the server:**
   ```bash
   # Using uvicorn directly
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   
   # Or using the main.py file
   python main.py
   ```

5. **API Documentation:**
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Set up environment:**
   ```bash
   echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
   ```

4. **Run the development server:**
   ```bash
   npm run dev
   # or
   yarn dev
   ```

5. **Open your browser:**
   - Frontend: http://localhost:3000

## 📊 API Endpoints

### Emissions
- `GET /api/emissions/activities` - Get all available activities
- `GET /api/emissions/categories` - Get activity categories
- `POST /api/emissions/calculate` - Calculate CO₂ emissions
- `GET /api/emissions/history/{email}` - Get user's calculation history

### Users
- `POST /api/users/subscribe` - Subscribe user for weekly tips
- `POST /api/users/unsubscribe` - Unsubscribe user
- `POST /api/users/send-tip` - Send weekly tip (testing)
- `GET /api/users/` - Get all users (admin)

## 🌱 Carbon Emission Factors

The application includes realistic emission factors for:

### Transportation
- Cars (gasoline, diesel, hybrid, electric)
- Public transport (bus, train, subway)
- Flights (domestic, international)
- Motorcycles, bicycles, walking

### Energy
- Grid electricity
- Natural gas
- Heating oil
- Propane

### Food
- Meat products (beef, pork, chicken, fish)
- Dairy and eggs
- Plant-based foods (vegetables, fruits, grains)

### Household
- Waste management
- Recycling and composting
- Water usage

## 🔧 Configuration

### Backend Environment Variables (.env)

```env
# Database
DATABASE_URL=postgresql://username:password@localhost/carbon_tracker_db
# For SQLite: sqlite:///./carbon_tracker.db

# Email Configuration
SENDGRID_API_KEY=your_sendgrid_api_key_here
FROM_EMAIL=noreply@yourapp.com

# Redis (for background tasks)
REDIS_URL=redis://localhost:6379/0

# CORS
ALLOWED_ORIGINS=http://localhost:3000,https://your-domain.com

# Security
SECRET_KEY=your-super-secret-key-change-this
```

### Frontend Environment Variables (.env.local)

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🚀 Deployment

### Backend Deployment

#### Option 1: Railway
1. Connect your GitHub repository
2. Set environment variables in Railway dashboard
3. Deploy automatically

#### Option 2: Render
1. Create new Web Service
2. Connect repository
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

#### Option 3: Docker
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Frontend Deployment

#### Option 1: Vercel
```bash
npm i -g vercel
vercel --prod
```

#### Option 2: Netlify
1. Build command: `npm run build`
2. Publish directory: `out` (after adding `next.config.js` export config)

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 📝 Development Notes

### Adding New Activities
1. Edit `backend/app/emission_factors.json`
2. Add new category or activity with emission factor
3. Restart backend server

### Email Integration
- Currently uses mock email service
- Integrate with SendGrid, Mailgun, or SMTP for production
- Update `backend/app/services/email_service.py`

### Database Schema
- Users table: email, subscription status
- Activities table: user activities and calculated emissions
- Automatic table creation on startup

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🌟 Features Roadmap

- [ ] User authentication and profiles
- [ ] Carbon offset recommendations
- [ ] Data visualization charts
- [ ] Mobile app (React Native)
- [ ] Social sharing features
- [ ] Corporate carbon tracking
- [ ] AI-powered recommendations

## 🐛 Known Issues

- Email service is mocked (needs real integration)
- No user authentication (planned for v2)
- Limited to basic emission factors (expandable)

## 💬 Support

For support and questions:
- Open an issue on GitHub
- Contact: your-email@example.com

---

**Built with ❤️ for a sustainable future** 🌍