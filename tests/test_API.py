from fastapi.testclient import TestClient
from chatroom_project.api import app
import chatroom_project.models as crpM

client = TestClient(app)

def test_root_not_found():
    response = client.get('/')
    assert response.status_code == 404

def test_post_message():
    to_send = crpM.MessageIn("Beta_Tester","ça passe ou ça casse")
    recived = client.post("/message/1", json = to_send.model_dump(mode="json"))
    assert recived.status_code == 200