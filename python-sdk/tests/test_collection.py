import pytest
import responses
from unibase import Unibase

@pytest.fixture
def db():
    return Unibase("http://localhost:5000", "ub_live_test_key")

@responses.activate
def test_collection_add(db):
    responses.add(
        responses.POST,
        "http://localhost:5000/api/collections",
        json={"success": True, "message": "Document added", "data": {"id": "doc1"}},
        status=200
    )
    
    res = db.collection("items").add({"name": "Test"})
    assert res.success is True
    
    req = responses.calls[0].request
    assert b"add_doc" in req.body
    assert b"items" in req.body

@responses.activate
def test_collection_query(db):
    responses.add(
        responses.POST,
        "http://localhost:5000/api/collections",
        json={"success": True, "message": "Success", "data": []},
        status=200
    )
    
    res = db.collection("items").where("price", ">", 100).get()
    assert res.success is True
    
    req = responses.calls[0].request
    assert b"query_docs" in req.body
    assert b"price" in req.body
