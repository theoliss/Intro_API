from fastapi.testclient import TestClient
from chatroom_project.api import app
import chatroom_project.models as crpM

client = TestClient(app)

def test_root_not_found():
    response = client.get('/')
    assert response.status_code == 404

def test_create_chatroom():
    room_to_send = crpM.ChatRoomIn(name = "test_room")
    received = client.post('/chatroom', json= room_to_send.model_dump(mode="jason"))
    assert received.json()['name'] ==  "test_room"
    assert received.status_code == 200

def test_delete_chatroom():
    received = client.delete('/chatroom/CetteIdNExistePas')
    assert received.status_code == 404

def post_message():
    to_send = crpM.MessageIn(author = "Beta_Tester", message = "ça passe ou ça casse")
    recived = client.post("/message/0", json = to_send.model_dump(mode="json"))
    assert recived.status_code == 200