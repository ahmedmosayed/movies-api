import httpx
from typing import List, Optional
from models.movie import Movie
from fastapi import HTTPException

OMDB_API_KEY = "1a614c5"
OMDB_API_URL = "http://www.omdbapi.com/"

async def search_omdb(title: str, genre: Optional[str] = None, actor: Optional[str] = None) -> List[Movie]:
    movies = []

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(OMDB_API_URL, params={"apikey": OMDB_API_KEY, "s": title})

            if response.status_code != 200:
                raise HTTPException(status_code=502, detail="OMDB API request failed.")

            data = response.json()
            if data.get("Response") != "True":
                return []  

            for item in data.get("Search", []):
                imdb_id = item.get("imdbID")
                if not imdb_id:
                    continue

                details_response = await client.get(OMDB_API_URL, params={"apikey": OMDB_API_KEY, "i": imdb_id})
                if details_response.status_code != 200:
                    continue

                detail = details_response.json()

                if (
                    (not genre or genre.lower() in detail.get("Genre", "").lower()) and
                    (not actor or actor.lower() in detail.get("Actors", "").lower())
                ):
                    movie = Movie(
                        id=detail.get("imdbID"),
                        title=detail.get("Title"),
                        year=detail.get("Year"),
                        type=detail.get("Type"),
                        genre=detail.get("Genre"),
                        actors=detail.get("Actors"),
                        source="OMDB"
                    )
                    movies.append(movie)

    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="Unable to reach OMDB service.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

    return movies
