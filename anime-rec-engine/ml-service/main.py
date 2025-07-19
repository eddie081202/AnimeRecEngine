from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Anime Recommendation ML Service",
    description="AI-powered anime recommendation engine",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class RecommendationRequest(BaseModel):
    user_id: Optional[str] = None
    liked_anime: List[str]
    disliked_anime: Optional[List[str]] = []
    genres: Optional[List[str]] = []
    mood: Optional[str] = None
    limit: Optional[int] = 10

class RecommendationResponse(BaseModel):
    recommendations: List[dict]
    explanations: List[str]
    confidence_scores: List[float]

class SearchRequest(BaseModel):
    query: str
    limit: Optional[int] = 20

@app.get("/")
async def root():
    return {"message": "Anime Recommendation ML Service"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "ml-recommendation"}

@app.post("/recommend", response_model=RecommendationResponse)
async def get_recommendations(request: RecommendationRequest):
    """
    Get personalized anime recommendations based on user preferences
    """
    try:
        # TODO: Implement recommendation logic
        # This is a placeholder implementation
        mock_recommendations = [
            {
                "id": "1",
                "title": "Attack on Titan",
                "genre": ["Action", "Drama"],
                "rating": 9.0,
                "synopsis": "Humanity's last stand against giant titans"
            },
            {
                "id": "2", 
                "title": "Death Note",
                "genre": ["Thriller", "Mystery"],
                "rating": 8.8,
                "synopsis": "A student finds a notebook that can kill people"
            }
        ]
        
        mock_explanations = [
            "Recommended because you liked similar action-packed anime with complex storylines",
            "Based on your preference for psychological thrillers and strategic thinking"
        ]
        
        mock_confidence = [0.85, 0.78]
        
        return RecommendationResponse(
            recommendations=mock_recommendations,
            explanations=mock_explanations,
            confidence_scores=mock_confidence
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/search")
async def search_anime(request: SearchRequest):
    """
    Search for anime using semantic similarity
    """
    try:
        # TODO: Implement semantic search
        return {
            "results": [],
            "query": request.query,
            "total": 0
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/explain/{anime_id}")
async def explain_recommendation(anime_id: str, user_id: Optional[str] = None):
    """
    Get AI-powered explanation for why an anime is recommended
    """
    try:
        # TODO: Implement GPT-4 explanation
        return {
            "anime_id": anime_id,
            "explanation": "This anime is recommended because it matches your taste for action-packed stories with complex characters and emotional depth.",
            "confidence": 0.85
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8001,
        reload=True
    ) 