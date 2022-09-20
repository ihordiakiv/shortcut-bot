from fastapi import APIRouter

from src.api.epics import views

router = APIRouter(tags=["Epics"], prefix="/epics")

router.add_api_route(
    "/",
    status_code=200,
    methods=["GET"],
    endpoint=views.list,
    summary="List Epics",
    description="List Epics returns a list of all Epics and their attributes.",
)

router.add_api_route(
    "/{epic_public_id}",
    status_code=200,
    methods=["GET"],
    endpoint=views.get,
    summary="Get Epic",
    description="Get Epic returns information about the selected Epic."
)

router.add_api_route(
    "/{epic_public_id}/stories",
    status_code=200,
    methods=["GET"],
    endpoint=views.get_stories,
    summary="List Epic Stories",
    description="Get a list of all Stories in an Epic."
)