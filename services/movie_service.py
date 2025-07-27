from typing import List, Optional
from models.movie import Movie
from services.omdb_service import search_omdb
from services.tmdb_service import search_tmdb

async def search_movies(title: str, genre: Optional[str] = None, actor: Optional[str] = None) -> List[Movie]:
    omdb_results = await search_omdb(title, genre, actor)
    tmdb_results = await search_tmdb(title)

    all_results = omdb_results + tmdb_results

    filtered_results = []

    for movie in all_results:
        if genre and movie.genre and genre.lower() not in movie.genre.lower():
            continue
        if actor and movie.actors and actor.lower() not in movie.actors.lower():
            continue
        filtered_results.append(movie)

    return filtered_results
