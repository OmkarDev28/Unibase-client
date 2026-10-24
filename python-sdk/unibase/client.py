import requests
from typing import Dict, Any

from .response import UnibaseResponse
from .exceptions import NetworkError

from .services import AuthService, QueryService, GraphService, StorageService, CollectionRef

class Unibase:
    """The main client for the Unibase SDK."""
    def __init__(self, url: str, api_key: str):
        self.url = url.rstrip('/')
        self.api_key = api_key
        
        self._session = requests.Session()
        self._session.headers.update({
            "Content-Type": "application/json",
            "ub-api-key": self.api_key
        })

        self.auth = AuthService(self)
        self.query = QueryService(self)
        self.graph = GraphService(self)
        self.storage = StorageService(self)

    def collection(self, name: str) -> CollectionRef:
        """Get a reference to a Unibase Collection for NoSQL operations."""
        return CollectionRef(name, self)

    def _execute_request(self, endpoint: str, payload: Dict[str, Any]) -> UnibaseResponse:
        try:
            res = self._session.post(endpoint, json=payload)
            try:
                data = res.json()
            except ValueError:
                data = {"success": False, "message": res.text, "data": None}
            return UnibaseResponse.from_dict(data, status_code=res.status_code)
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Failed to connect to Unibase: {str(e)}")
