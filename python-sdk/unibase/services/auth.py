from ._base import _BaseService
from ..response import UnibaseResponse

class AuthService(_BaseService):
    def create_user(self, username: str, password: str, email: str, **kwargs) -> UnibaseResponse:
        """Create a new user in the Unibase authentication system."""
        data = {
            "username": username,
            "password": password,
            "email": email
        }
        data.update(kwargs)
        return self._request("/api/auth", {
            "action": "create_user",
            "data": data
        })

    def login(self, username: str, password: str) -> UnibaseResponse:
        """Authenticate a user and return their session details."""
        return self._request("/api/auth", {
            "action": "login_with_username",
            "data": {
                "username": username,
                "password": password
            }
        })

    def get_user_id(self, username: str) -> UnibaseResponse:
        """Retrieve a user's unique ID by their username."""
        return self._request("/api/auth", {
            "action": "get_id",
            "data": {
                "username": username
            }
        })

    def update_user(self, user_id: str, **fields) -> UnibaseResponse:
        """Update an existing user's fields."""
        data = {
            "user_id": user_id
        }
        data.update(fields)
        return self._request("/api/auth", {
            "action": "update_user",
            "data": data
        })
