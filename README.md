# Anime Recommendation Engine

A personalized anime recommendation system that suggests shows based on your watch history and ratings.

## Features

- User authentication and profile management
- Watchlist management (add/remove anime)
- Rating system for watched shows
- Personalized recommendations using collaborative filtering
- Trending anime feed
- Modern, responsive UI with React and Tailwind CSS

## Tech Stack

- Frontend: React + Tailwind CSS
- Backend: Node.js + Express
- Database: MongoDB
- ML Service: Python with scikit-surprise/TensorFlow
- API Integration: Jikan/AniList API for anime data

## Project Structure

```
/anime-rec-engine
├── /frontend          # React frontend application
├── /backend          # Node.js + Express backend
├── /ml-service       # Python ML microservice
├── /docs            # Documentation
└── /scripts         # Utility scripts
```

## Getting Started

### Prerequisites

- Node.js (v18 or higher)
- Python 3.8+
- MongoDB
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd anime-rec-engine
```

2. Install frontend dependencies:
```bash
cd frontend
npm install
```

3. Install backend dependencies:
```bash
cd ../backend
npm install
```

4. Install ML service dependencies:
```bash
cd ../ml-service
pip install -r requirements.txt
```

5. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

### Running the Application

1. Start the backend server:
```bash
cd backend
npm run dev
```

2. Start the frontend development server:
```bash
cd frontend
npm run dev
```

3. Start the ML service:
```bash
cd ml-service
python app.py
```

## Development

- Frontend runs on: http://localhost:3000
- Backend API runs on: http://localhost:8000
- ML Service runs on: http://localhost:5000

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 