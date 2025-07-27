from fastapi import APIRouter, Query
from typing import List, Optional
from services.movie_service import search_movies
from models.movie import Movie

router = APIRouter(prefix="/api/movies", tags=["Movies"])

@router.get("/search", response_model=List[Movie])
async def search_movies_route(
    title: str = Query(..., description="Movie title to search for"),
    genre: Optional[str] = Query(None, description="Filter by genre"),
    actor: Optional[str] = Query(None, description="Filter by actor")
):
    return await search_movies(title=title, genre=genre, actor=actor)
