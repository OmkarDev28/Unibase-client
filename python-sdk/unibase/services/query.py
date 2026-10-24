from typing import Optional, List, Dict, Any
from ._base import _BaseService
from ..response import UnibaseResponse
from ..utils import dict_to_conditions

class QueryService(_BaseService):
    def raw(self, sql: str, params: Optional[list] = None) -> UnibaseResponse:
        """Execute a raw SQL query with optional parameters."""
        return self._request("/api/query", {
            "action": "raw_sql",
            "sql": sql,
            "params": params or []
        })

    def select(self, table: str, columns: Optional[list] = None, where: Optional[Dict[str, Any]] = None) -> UnibaseResponse:
        """Select rows from a table."""
        payload = {
            "action": "SELECT",
            "table": table,
            "columns": columns or ["*"]
        }
        if where:
            payload["conditions"] = dict_to_conditions(where)
        return self._request("/api/query", payload)

    def insert(self, table: str, values: Dict[str, Any]) -> UnibaseResponse:
        """Insert a row into a table."""
        return self._request("/api/query", {
            "action": "INSERT",
            "table": table,
            "values": values
        })

    def update(self, table: str, set: Dict[str, Any], where: Optional[Dict[str, Any]] = None) -> UnibaseResponse:
        """Update rows in a table."""
        payload = {
            "action": "UPDATE",
            "table": table,
            "updates": set
        }
        if where:
            payload["conditions"] = dict_to_conditions(where)
        return self._request("/api/query", payload)

    def delete(self, table: str, where: Optional[Dict[str, Any]] = None) -> UnibaseResponse:
        """Delete rows from a table."""
        payload = {
            "action": "DELETE",
            "table": table
        }
        if where:
            payload["conditions"] = dict_to_conditions(where)
        return self._request("/api/query", payload)
