from fastapi import APIRouter

from src.api.stories import views

router = APIRouter(tags=["Stories"], prefix="/stories")

router.add_api_route(
        "/{story_public_id}",
        status_code=200,
        methods=["GET"],
        endpoint=views.get,
        summary="Get Story",
        description="Get Story returns information about a chosen Story."
)