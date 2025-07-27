# models/movie.py
from pydantic import BaseModel
from typing import Optional

class Movie(BaseModel):
    id: str
    title: str
    year: Optional[str]
    type: Optional[str]
    genre: Optional[str]
    actors: Optional[str]
    source: str
