from fastapi import FastAPI
from routers import movie_router

app = FastAPI()
app.include_router(movie_router.router)
