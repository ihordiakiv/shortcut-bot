from typing import List

from conf.config import conf
from src.client.http_client import HttpClientMixin
from src.client.utils import response_decorator


class ShortcutClient(HttpClientMixin):
    _headers: dict = {"Accept-Version": "4.4.0"}

    def __init__(self, base_url, api_version: str = "v3"):
        self.base_url = base_url
        self.api_version = api_version

    @response_decorator
    async def list(self, *, token, prefix, params=None) -> List:
        endpoint = f"{self.base_url}/{self.api_version}/{prefix}"
        response = await self._get(endpoint, token, params)
        return response

    @response_decorator
    async def get(self, *, token, prefix, id: int, suffix: str = None, params: dict = None):
        if suffix:
            endpoint = f"{self.base_url}/{self.api_version}/{prefix}/{id}/{suffix}"
        else:
            endpoint = f"{self.base_url}/{self.api_version}/{prefix}/{id}"
        response = await self._get(endpoint, token, params)
        return response


shortcut_client = ShortcutClient(base_url=conf.SHORTCUT_API_URL)
