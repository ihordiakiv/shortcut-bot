from fastapi import APIRouter

from src.api.milestones import views

router = APIRouter(tags=["Milestones"], prefix="/milestones")

router.add_api_route(
    "/",
    status_code=200,
    methods=["GET"],
    endpoint=views.list,
    summary="List Milestones",
    description="List Milestones returns a list of all Milestones and their attributes."
)

router.add_api_route(
    "/{milestone_public_id}",
    status_code=200,
    methods=["GET"],
    endpoint=views.get,
    summary="Get Milestone",
    description="Get Milestone returns information about a chosen Milestone."
)

router.add_api_route(
    "/{milestone_public_id}/epics",
    status_code=200,
    methods=["GET"],
    endpoint=views.get_epics,
    summary="List Milestone Epics",
    description="List all of the Epics within the Milestone."
)