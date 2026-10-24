from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables
from routes.reviews import router as reviews_router
from exceptions import PlayNameNotFoundError,ReviewNotFoundError, review_not_found_handler,play_name_not_found_handler

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    print("Database tables created")
    yield
    # Shutdown: cleanup here
    print("Shutting down the app")


app = FastAPI(
    title="Theater Star",
    description="Theater reviews API for Theater Star",
    lifespan=lifespan,
)

app.include_router(reviews_router)

app.add_exception_handler(PlayNameNotFoundError, play_name_not_found_handler)
app.add_exception_handler(ReviewNotFoundError, review_not_found_handler)

@app.get("/")
def root():
    return {"message": "Welcome to Theater Star review API"}