import os
import pytest
import responses
from unibase import Unibase

@pytest.fixture
def db():
    return Unibase("http://localhost:5000", "ub_live_test_key")

@responses.activate
def test_storage_upload(db, tmp_path):
    # Create a temporary file
    test_file = tmp_path / "test.txt"
    test_file.write_text("hello world")
    
    responses.add(
        responses.POST,
        "http://localhost:5000/api/storage/upload",
        json={"success": True, "message": "Uploaded", "data": {"url": "/uploads/test.txt"}},
        status=200
    )
    
    res = db.storage.upload(str(test_file))
    assert res.success is True
    assert res.data["url"] == "/uploads/test.txt"
    
    # Verify request payload
    req = responses.calls[0].request
    assert b"hello world" in req.body
