from datetime import datetime

from fastapi import Path

from src.client.shortcut_client import shortcut_client
from conf.config import conf
from src.client.utils import save_exel

path = "stories"

async def get(story_public_id: int = Path(description="The ID of the Story.")):
    response = await shortcut_client.get(token=conf.SHORTCUT_API_TOKEN, prefix=path, id=story_public_id)

    file_name = f'get_{story_public_id}_{datetime.now()}.xlsx'
    await save_exel(path, response, file_name)

    return response