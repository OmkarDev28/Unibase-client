from typing import Optional, Dict, Any
from ._base import _BaseService
from ..response import UnibaseResponse

class GraphService(_BaseService):
    def create_node(self, name: str, properties: Optional[Dict[str, Any]] = None) -> UnibaseResponse:
        """Create a new node in the graph."""
        return self._request("/api/graph", {
            "action": "CREATE_NODE",
            "node_name": name,
            "properties": properties or {}
        })

    def create_relationship(self, from_node: str, to_node: str, relationship: str, properties: Optional[Dict[str, Any]] = None) -> UnibaseResponse:
        """Create a directed relationship between two nodes."""
        return self._request("/api/graph", {
            "action": "CREATE_RELATIONSHIP",
            "from_node": from_node,
            "to_node": to_node,
            "relationship": relationship,
            "properties": properties or {}
        })

    def delete_relationship(self, from_node: str, to_node: str, relationship: str) -> UnibaseResponse:
        """Delete a relationship between two nodes."""
        return self._request("/api/graph", {
            "action": "DELETE_RELATIONSHIP",
            "from_node": from_node,
            "to_node": to_node,
            "relationship": relationship
        })

    def get_neighbors(self, node: str, relationship: str) -> UnibaseResponse:
        """Get all nodes connected to a specific node by a specific relationship."""
        return self._request("/api/graph", {
            "action": "GET_NEIGHBORS",
            "node_name": node,
            "relationship": relationship
        })
