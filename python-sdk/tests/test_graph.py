import pytest
import responses
from unibase import Unibase

@pytest.fixture
def db():
    return Unibase("http://localhost:5000", "ub_live_test_key")

@responses.activate
def test_create_node(db):
    responses.add(
        responses.POST,
        "http://localhost:5000/api/graph",
        json={"success": True, "message": "Node created", "data": None},
        status=200
    )
    
    res = db.graph.create_node("Bharat", {"age": 25, "country": "India"})
    assert res.success is True
    
    req = responses.calls[0].request
    assert b"CREATE_NODE" in req.body
    assert b"Bharat" in req.body

@responses.activate
def test_create_relationship(db):
    responses.add(
        responses.POST,
        "http://localhost:5000/api/graph",
        json={"success": True, "message": "Relationship created", "data": None},
        status=200
    )
    
    res = db.graph.create_relationship("Bharat", "Aarav", "FRIENDS_WITH")
    assert res.success is True
    
    req = responses.calls[0].request
    assert b"CREATE_RELATIONSHIP" in req.body
    assert b"FRIENDS_WITH" in req.body
