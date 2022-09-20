from typing import Optional, Dict, Union
from fastapi.security import HTTPAuthorizationCredentials
from httpx import AsyncClient


class HttpClientMixin:

    @staticmethod
    def __get_auth_header(token, headers: dict = None):
        auth_header = {
            "Shortcut-Token": token,
            "Content-Type": "application/json",
        }
        if headers is None:
            return auth_header
        headers.update(auth_header)
        return headers

    @staticmethod
    async def _get(
        endpoint: str,
        token: Optional[HTTPAuthorizationCredentials] = None,
        params: Optional[Dict[str, Union[str, list]]] = None,
        headers: dict = None,
    ):
        headers = HttpClientMixin.__get_auth_header(token, headers)
        async with AsyncClient() as client:
            response = await client.get(endpoint, params=params, headers=headers, timeout=None)
        return response