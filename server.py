import uvicorn
from fastapi import FastAPI

from conf.config import conf
from src.api.milestones.router import router as milestones_router
from src.api.workflows.router import router as workflows_router
from src.api.epics.router import router as epics_router
from src.api.groups.router import router as groups_router
from src.api.members.router import router as members_router
from src.api.stories.router import router as stories_router


def create_app():
    _app = FastAPI(
            title=conf.PROJECT_NAME,
            openapi_url=conf.OPENAPI_URL,
            docs_url=conf.DOCS_URL,
            redoc_url=conf.REDOC_URL,
    )

    @_app.get(f"{conf.ROOT_PATH}{conf.OPENAPI_URL}")
    async def open_api():
        return _app.openapi()

    _app.include_router(milestones_router)
    _app.include_router(workflows_router)
    _app.include_router(epics_router)
    _app.include_router(groups_router)
    _app.include_router(members_router)
    _app.include_router(stories_router)
    return _app


app = create_app()


if __name__ == '__main__':
    uvicorn.run('server:app',
                host="0.0.0.0",
                port=8080,
                reload=True,
                root_path=conf.ROOT_PATH)
