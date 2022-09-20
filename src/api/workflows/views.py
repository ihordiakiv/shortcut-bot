from datetime import datetime

from fastapi import Query, Path

from src.api.workflows.enums import Name, Type, Verb
from src.client.shortcut_client import shortcut_client
from conf.config import conf
from src.client.utils import save_exel, base_filter

path = 'workflows'


async def list(name: Name | None = Query(default=None,
                                         description="The Workflow State’s name."),
               type: Type | None= Query(default=None,
                                        description="The type of Workflow State."),
               verb: Verb | None = Query(default=None,
                                         description="The verb that triggers a move to that Workflow "
                                                     "State when making VCS commits."),
               ):
    response = await shortcut_client.list(token=conf.SHORTCUT_API_TOKEN, prefix=path)

    name = f'r"{name}"' if name else None
    type = f'r"{type}"' if type else None
    verb = f'r"{verb}"' if verb else None

    params = {'name': name,
              'type': type,
              'verb': verb,
              }

    result = await base_filter(params, response, depth="states")
    file_name = f'list_{datetime.now()}.xlsx'
    await save_exel(path, result, file_name)

    return result


async def get(workflow_public_id: int = Path(description="The ID of the Workflow.")):
    response = await shortcut_client.get(token=conf.SHORTCUT_API_TOKEN, prefix=path, id=workflow_public_id)

    file_name = f'get_{workflow_public_id}_{datetime.now()}.xlsx'
    await save_exel(path, response, file_name)

    return response
