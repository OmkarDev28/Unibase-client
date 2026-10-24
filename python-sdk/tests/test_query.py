import pytest
import responses
from unibase import Unibase

@pytest.fixture
def db():
    return Unibase("http://localhost:5000", "ub_live_test_key")

@responses.activate
def test_select_query(db):
    responses.add(
        responses.POST,
        "http://localhost:5000/api/query",
        json={"success": True, "message": "Success", "data": [{"id": 1, "name": "Bharat"}]},
        status=200
    )
    
    res = db.query.select("users", ["id", "name"], {"role": "admin"})
    assert res.success is True
    assert len(res.data) == 1
    
    # Verify request payload
    req = responses.calls[0].request
    assert b"SELECT" in req.body
    assert b"conditions" in req.body
