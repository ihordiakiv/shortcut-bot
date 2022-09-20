from datetime import datetime

from fastapi import Query, Path

from src.api.epics.enums import StoryType
from src.api.milestones.enums import State
from src.client.shortcut_client import shortcut_client
from conf.config import conf
from src.client.utils import save_exel, base_filter

path = 'epics'


async def list(archived: bool | None = Query(default=None,
                                             description="True/false boolean that indicates whether "
                                                         "the Epic is archived or not."),
               started: bool | None = Query(default=None,
                                            description="A true/false boolean indicating "
                                                        "if the Epic has been started."),
               completed: bool | None = Query(default=None,
                                              description="A true/false boolean indicating "
                                                          "if the Epic has been completed."),
               state: State | None = Query(default=None,
                                           description="The workflow state that the Epic is in.",
                                           deprecated=True)
               ):
    response = await shortcut_client.list(token=conf.SHORTCUT_API_TOKEN,
                                          prefix=path,)

    state = f'r"{state}"' if state else None
    params = {'archived': archived,
              'started': started,
              'completed': completed,
              'state': state}

    result = await base_filter(params, response)
    file_name = f'list_{datetime.now()}.xlsx'
    await save_exel(path, result, file_name)

    return result


async def get(epic_public_id: int = Path(description="The unique ID of the Epic.")):
    response = await shortcut_client.get(token=conf.SHORTCUT_API_TOKEN,
                                         prefix=path,
                                         id=epic_public_id)

    file_name = f'get_{epic_public_id}_{datetime.now()}.xlsx'
    await save_exel(path, response, file_name)

    return response


async def get_stories(epic_public_id: int = Path(description="The unique ID of the Epic."),
                      archived: bool | None = Query(default=None,
                                                    description="True if the story has been archived or not."),
                      started: bool | None = Query(default=None,
                                                   description="A true/false boolean indicating "
                                                               "if the Story has been started."),
                      completed: bool | None = Query(default=None,
                                                     description="A true/false boolean indicating "
                                                                 "if the Story has been completed."),
                      blocked: bool | None = Query(default=None,
                                                   description="A true/false boolean indicating "
                                                               "if the Story is currently blocked."),
                      bloker: bool | None = Query(default=None,
                                                  description="A true/false boolean indicating "
                                                              "if the Story is currently a blocker of another story."),
                      story_type: StoryType | None = Query(default=None,
                                                           description="The type of story (feature, bug, chore)."),
                      ):
    response = await shortcut_client.get(token=conf.SHORTCUT_API_TOKEN,
                                         prefix=path,
                                         id=epic_public_id,
                                         suffix="stories")
    story_type = f'r"{story_type}"' if story_type else None
    params = {'archived': archived,
              'started': started,
              'completed': completed,
              'blocked': blocked,
              'blocker': bloker,
              'story_type': story_type}

    result = await base_filter(params, response)

    file_name = f'list_epics_{epic_public_id}_{datetime.now()}.xlsx'
    await save_exel(path, result, file_name)

    return result
