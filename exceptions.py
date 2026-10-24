from fastapi import Request
from fastapi.responses import JSONResponse

class PlayNameNotFoundError(Exception):
    def __init__(self, play_name: str):
        self.play_name = play_name


class ReviewNotFoundError(Exception):
    def __init__(self, review_id: int):
        self.review_id = review_id


async def play_name_not_found_handler(request: Request, exc: ReviewNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error": "play_name_not_found",
            "message": f"No review found for {exc.play_name}",
            "play_name": exc.play_name,
        }
    )


async def review_not_found_handler(request: Request, exc: ReviewNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error": "review_not_found",
            "message": f"No review found for {exc.review_id}",
            "review_id": exc.review_id,
        }
    )