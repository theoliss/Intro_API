from fastapi.testclient import TestClient
from chatroom_project.api import app

client = TestClient(app)

def test_root_not_found():
    response = client.get('/')
    assert response.status_code == 404

