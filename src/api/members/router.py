from fastapi import APIRouter

from src.api.members import views

router = APIRouter(tags=["Members"], prefix="/members")

router.add_api_route(
    "/",
    status_code=200,
    methods=["GET"],
    endpoint=views.list,
    summary="List Members",
    description="Returns information about members of the Workspace."
)

router.add_api_route(
    "/{member_public_id}",
    status_code=200,
    methods=["GET"],
    endpoint=views.get,
    summary="Get Member",
    description="Returns information about a Member."
)