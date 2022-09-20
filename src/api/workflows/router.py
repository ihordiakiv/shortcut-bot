from fastapi import APIRouter

from src.api.workflows import views

router = APIRouter(tags=["Workflows"], prefix="/workflows")

router.add_api_route(
    "/",
    status_code=200,
    methods=["GET"],
    endpoint=views.list,
    summary="List Workflows",
    description="Returns a list of all Workflows in the Workspace."
)

router.add_api_route(
    "/{workflow_public_id}",
    status_code=200,
    methods=["GET"],
    endpoint=views.get,
    summary="Get Workflow",
    description="Get Workflow returns information about a chosen Workflow."
)