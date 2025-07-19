# 🎌 Anime Recommendation Engine

A sophisticated anime recommendation system that combines collaborative filtering, content-based filtering, and AI-powered insights to help users discover their next favorite anime.

## ✨ Features

### Core Features
- **Personalized Recommendations**: Based on user watch history and ratings
- **AI-Powered Insights**: GPT-4 explanations for why anime are recommended
- **Advanced Search**: Fuzzy search with ElasticSearch integration
- **Mood-Based Filtering**: Find anime based on emotional themes
- **Real-time Updates**: WebSocket integration for live recommendations
- **Beautiful UI**: Modern, responsive design with Framer Motion animations

### Technical Features
- **Multi-Service Architecture**: Frontend, Backend, ML Service
- **AI/ML Integration**: Collaborative filtering + Content-based filtering
- **NLP Processing**: Sentence-BERT for semantic similarity
- **Scalable Infrastructure**: Docker, CI/CD, Cloud deployment ready
- **Type Safety**: Full TypeScript implementation

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   ML Service    │
│   (Next.js)     │◄──►│   (NestJS)      │◄──►│   (FastAPI)     │
│                 │    │                 │    │                 │
│ • React + TS    │    │ • REST API      │    │ • ML Models     │
│ • Tailwind CSS  │    │ • Auth          │    │ • NLP           │
│ • Framer Motion │    │ • Database      │    │ • OpenAI        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │   Database      │
                    │                 │
                    │ • PostgreSQL    │
                    │ • Redis         │
                    │ • ElasticSearch │
                    └─────────────────┘
```

## 🛠️ Tech Stack

### Frontend
- **Next.js 15** - React framework with SSR
- **TypeScript** - Type safety
- **Tailwind CSS** - Utility-first CSS
- **Framer Motion** - Animations
- **Radix UI** - Accessible components
- **React Query** - Data fetching
- **Chart.js** - Data visualization

### Backend
- **NestJS** - Modular Node.js framework
- **Prisma** - Type-safe database ORM
- **PostgreSQL** - Primary database
- **Redis** - Caching layer
- **JWT** - Authentication
- **Swagger** - API documentation

### ML Service
- **FastAPI** - Python web framework
- **scikit-learn** - Machine learning
- **sentence-transformers** - NLP embeddings
- **OpenAI API** - GPT-4 integration
- **pandas/numpy** - Data processing

### Infrastructure
- **Docker** - Containerization
- **GitHub Actions** - CI/CD
- **Railway/Render** - Deployment
- **ElasticSearch** - Search engine

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.8+
- PostgreSQL
- Redis
- Docker (optional)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/anime-rec-engine.git
cd anime-rec-engine
```

2. **Frontend Setup**
```bash
cd frontend
npm install
npm run dev
```

3. **Backend Setup**
```bash
cd backend
npm install
npm run start:dev
```

4. **ML Service Setup**
```bash
cd ml-service
source venv/bin/activate
uvicorn main:app --reload
```

5. **Environment Variables**
```bash
# Frontend (.env.local)
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_ML_SERVICE_URL=http://localhost:8001

# Backend (.env)
DATABASE_URL="postgresql://..."
REDIS_URL="redis://..."
JWT_SECRET="your-secret"

# ML Service (.env)
OPENAI_API_KEY="your-openai-key"
```

## 📁 Project Structure

```
anime-rec-engine/
├── frontend/                 # Next.js application
│   ├── src/
│   │   ├── app/            # App router pages
│   │   ├── components/     # Reusable components
│   │   ├── lib/           # Utilities and configs
│   │   └── types/         # TypeScript types
│   └── public/            # Static assets
├── backend/                # NestJS API
│   ├── src/
│   │   ├── modules/       # Feature modules
│   │   ├── common/        # Shared utilities
│   │   └── config/        # Configuration
│   └── prisma/           # Database schema
├── ml-service/            # Python ML service
│   ├── app/
│   │   ├── models/        # ML models
│   │   ├── services/      # Business logic
│   │   └── api/          # FastAPI routes
│   └── data/             # Training data
└── infra/                # Infrastructure
    ├── docker/           # Docker configs
    └── k8s/             # Kubernetes manifests
```

## 🎯 Core Features Implementation

### 1. Recommendation Engine
- **Collaborative Filtering**: User-based and item-based recommendations
- **Content-Based Filtering**: Based on anime features (genre, tags, synopsis)
- **Hybrid Approach**: Combines both methods for better accuracy

### 2. AI Integration
- **GPT-4 Explanations**: Why this anime is recommended
- **Semantic Search**: Using sentence-transformers
- **Mood Analysis**: Emotional theme detection

### 3. Advanced Search
- **Fuzzy Matching**: ElasticSearch for typo tolerance
- **Semantic Search**: Find similar anime by description
- **Filter Combinations**: Genre, year, rating, episodes

### 4. User Experience
- **Real-time Updates**: WebSocket for live recommendations
- **Personalized Dashboard**: User taste analysis
- **Social Features**: Share recommendations

## 🔧 Development

### Running Tests
```bash
# Frontend
npm run test

# Backend
npm run test

# ML Service
pytest
```

### Database Migrations
```bash
cd backend
npx prisma migrate dev
```

### Docker Development
```bash
docker-compose up -d
```

## 🚀 Deployment

### Frontend (Vercel)
```bash
npm run build
vercel --prod
```

### Backend (Railway)
```bash
railway login
railway up
```

### ML Service (Fly.io)
```bash
flyctl launch
flyctl deploy
```

## 📊 Performance

- **Response Time**: < 200ms for recommendations
- **Search**: < 100ms with ElasticSearch
- **Scalability**: Horizontal scaling ready
- **Caching**: Redis for hot data

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

- Jikan API for anime data
- OpenAI for AI capabilities
- The anime community for inspiration

---

**Built with ❤️ for anime lovers everywhere** 