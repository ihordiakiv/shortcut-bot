from datetime import datetime

from fastapi import Query, Path
from pydantic import UUID4

from src.api.members.enums import Role
from src.client.shortcut_client import shortcut_client
from conf.config import conf
from src.client.utils import save_exel, base_filter

path = 'members'


async def list(role: Role | None = Query(default=None),
               disabled: bool | None = Query(default=None)):
    response = await shortcut_client.list(token=conf.SHORTCUT_API_TOKEN, prefix=path)
    role = f'r"{role}"' if role else None
    params = {'disabled': disabled,
              'role': role,
              }

    result = await base_filter(params, response)
    file_name = f'list_{datetime.now()}.xlsx'
    await save_exel(path, result, file_name)

    return result


async def get(member_public_id: UUID4 = Path(description="The Member’s unique ID.")):
    response = await shortcut_client.get(token=conf.SHORTCUT_API_TOKEN, prefix=path, id=member_public_id)

    file_name = f'get_{member_public_id}_{datetime.now()}.xlsx'
    await save_exel(path, response, file_name)

    return response
