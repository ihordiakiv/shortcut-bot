from fastapi import APIRouter

from src.api.groups import views

router = APIRouter(tags=["Groups"], prefix="/groups")

router.add_api_route(
    "/",
    status_code=200,
    methods=["GET"],
    endpoint=views.list,
    summary="List Groups",
    description="""A group in our API maps to a “Team” within the Shortcut Product. 
                  A Team is a collection of Users that can be associated to Stories, 
                    Epics, and Iterations within Shortcut.""",
)

router.add_api_route(
    "/{group_public_id}",
    status_code=200,
    methods=["GET"],
    endpoint=views.get,
    summary="Get Group",
    description=""
)

router.add_api_route(
    "/{epic_public_id}/stories",
    status_code=200,
    methods=["GET"],
    endpoint=views.get_stories,
    summary="List Group Stories",
    description="List the Stories assigned to the Group. (By default, limited to 1,000)."
)