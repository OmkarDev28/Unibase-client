import pytest
import responses
from unibase import Unibase

@pytest.fixture
def db():
    return Unibase("http://localhost:5000", "ub_live_test_key")

@responses.activate
def test_create_user(db):
    responses.add(
        responses.POST,
        "http://localhost:5000/api/auth",
        json={"success": True, "message": "User created", "data": {"id": "1", "username": "Bharat"}},
        status=200
    )
    
    res = db.auth.create_user("Bharat", "pass", "bharat@example.com")
    assert res.success is True
    assert res.data["username"] == "Bharat"
    
    # Verify request payload
    assert len(responses.calls) == 1
    req = responses.calls[0].request
    assert b"create_user" in req.body
