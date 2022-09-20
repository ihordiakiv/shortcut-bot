from datetime import datetime

from fastapi import Query, Path

from src.api.milestones.enums import State
from src.client.shortcut_client import shortcut_client
from conf.config import conf
from src.client.utils import save_exel, base_filter

path = 'milestones'


async def list(archived: bool | None = Query(default=None,
                                             description="A boolean indicating whether "
                                                         "the Milestone has been archived or not."),
               started: bool | None = Query(default=None,
                                            description="A true/false boolean indicating "
                                                        "if the Milestone has been started."),
               completed: bool | None = Query(default=None,
                                              description="A true/false boolean indicating "
                                                          "if the Milestone has been completed."),
               state: State | None = Query(default=None,
                                           description="The workflow state that the Milestone is in.")
               ):
    response = await shortcut_client.list(token=conf.SHORTCUT_API_TOKEN, prefix=path)
    state = f'r"{state}"' if state else None
    params = {'archived': archived,
              'started': started,
              'completed': completed,
              'state': state}

    result = await base_filter(params, response)
    file_name = f'list_{datetime.now()}.xlsx'
    await save_exel(path, result, file_name)

    return result


async def get(milestone_public_id: int = Path(description="The ID of the Milestone.")):
    response = await shortcut_client.get(token=conf.SHORTCUT_API_TOKEN, prefix=path, id=milestone_public_id)

    file_name = f'get_{milestone_public_id}_{datetime.now()}.xlsx'
    await save_exel(path, response, file_name)

    return response


async def get_epics(milestone_public_id: int = Path(description="The ID of the Milestone."),
                    archived: bool | None = Query(default=None,
                                                  description="A boolean indicating whether "
                                                              "the Milestone has been archived or not."),
                    started: bool | None = Query(default=None,
                                                 description="A true/false boolean indicating "
                                                             "if the Milestone has been started."),
                    completed: bool | None = Query(default=None,
                                                   description="A true/false boolean indicating "
                                                               "if the Milestone has been completed."),
                    state: State | None = Query(default=None,
                                                description="The workflow state that the Milestone is in."),
                    ):
    response = await shortcut_client.get(token=conf.SHORTCUT_API_TOKEN,
                                         prefix=path,
                                         id=milestone_public_id,
                                         suffix="epics")

    state = f'r"{state}"' if state else None
    params = {'archived': archived,
              'started': started,
              'completed': completed,
              'state': state}

    result = await base_filter(params, response)

    file_name = f'list_epics_{milestone_public_id}_{datetime.now()}.xlsx'
    await save_exel(path, result, file_name)

    return result
