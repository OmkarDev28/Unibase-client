from typing import Any, Dict
from ._base import _BaseService
from ..response import UnibaseResponse

class CollectionQuery:
    def __init__(self, collection_ref):
        self.collection_ref = collection_ref
        self._filters = []

    def where(self, field: str, op: str, value: Any) -> "CollectionQuery":
        """Add a filter condition to the query."""
        self._filters.append({
            "field": field,
            "operator": op,
            "value": value
        })
        return self

    def get(self) -> UnibaseResponse:
        """Execute the query and get matching documents."""
        return self.collection_ref._request("/api/collections", {
            "action": "query_docs",
            "collection": self.collection_ref._name,
            "filters": self._filters
        })

    def update(self, data: Dict[str, Any]) -> UnibaseResponse:
        """Update documents matching the query."""
        return self.collection_ref._request("/api/collections", {
            "action": "update_doc",
            "collection": self.collection_ref._name,
            "filters": self._filters,
            "data": data
        })

    def delete(self) -> UnibaseResponse:
        """Delete documents matching the query."""
        return self.collection_ref._request("/api/collections", {
            "action": "delete_doc",
            "collection": self.collection_ref._name,
            "filters": self._filters
        })

class DocRef:
    def __init__(self, doc_id: str, collection_ref):
        self.doc_id = doc_id
        self.collection_ref = collection_ref

    def delete(self) -> UnibaseResponse:
        """Delete this specific document by ID."""
        return self.collection_ref.where("id", "==", self.doc_id).delete()

class CollectionRef(_BaseService):
    def __init__(self, name: str, client):
        super().__init__(client)
        self._name = name

    def add(self, data: Dict[str, Any]) -> UnibaseResponse:
        """Add a new document to the collection."""
        return self._request("/api/collections", {
            "action": "add_doc",
            "collection": self._name,
            "data": data
        })

    def get_all(self) -> UnibaseResponse:
        """Get all documents in the collection."""
        return self._request("/api/collections", {
            "action": "get_all_docs",
            "collection": self._name
        })

    def where(self, field: str, op: str, value: Any) -> CollectionQuery:
        """Start a query with a filter condition."""
        return CollectionQuery(self).where(field, op, value)

    def doc(self, doc_id: str) -> DocRef:
        """Get a reference to a specific document by ID."""
        return DocRef(doc_id, self)
