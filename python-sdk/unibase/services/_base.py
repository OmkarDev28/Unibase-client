from typing import Any, Dict
from ..response import UnibaseResponse

class _BaseService:
    """
    Shared logic for all services (Auth, Collection, Graph, etc.)
    """
    def __init__(self, client):
        self._client = client

    def _request(self, endpoint_suffix: str, payload: Dict[str, Any]) -> UnibaseResponse:
        endpoint = f"{self._client.url}{endpoint_suffix}"
        return self._client._execute_request(endpoint, payload)
