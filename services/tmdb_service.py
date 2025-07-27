import httpx
from typing import List
from models.movie import Movie
from fastapi import HTTPException

TMDB_API_KEY = "794f2957d82f9d6faca03bfb16cce04e"
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"

async def search_tmdb(title: str) -> List[Movie]:
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(
                TMDB_SEARCH_URL,
                params={
                    "api_key": TMDB_API_KEY,
                    "query": title
                }
            )

        if response.status_code != 200:
            raise HTTPException(status_code=502, detail="TMDB API request failed.")

        data = response.json()

        if "results" not in data:
            raise HTTPException(status_code=500, detail="Invalid response from TMDB API.")

        movies = []
        for result in data["results"]:
            if not result.get("title"):
                continue

            movie = Movie(
                id=str(result.get("id")),
                title=result.get("title"),
                year=result.get("release_date", "")[:4] if result.get("release_date") else None,
                type="movie",
                genre=None,  
                actors=None,  
                source="TMDB"
            )
            movies.append(movie)

        return movies

    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="Unable to reach TMDB service.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
