from fastapi.testclient import TestClient
from chatroom_project.api import app
import chatroom_project.models as crpM

client = TestClient(app)

def test_root_not_found():
    response = client.get('/')
    assert response.status_code == 404

def test_create_chatroom():
    room_to_send = crpM.ChatRoomIn(name = "test_room")
    received = client.post('/chatroom', json = room_to_send.model_dump(mode="json"))
    assert received.json()['name'] ==  "test_room"

def test_delete_chatroom():
    room_to_send = crpM.ChatRoomIn(name = "test_room")
    received = client.post('/chatroom', json = room_to_send.model_dump(mode="json"))
    room_id = received.json()['uid']
    received = client.delete(f'/chatroom/{room_id}')
    assert received.status_code == 200

def test_get_chatrooms():
    #with an empty list
    response = client.get('/chatroom')
    assert response.status_code == 200

    #after adding a chatroom  
    room_to_send = crpM.ChatRoomIn(name = "test_room")
    client.post('/chatroom', json = room_to_send.model_dump(mode="json"))
    response = client.get('/chatroom')
    assert response.status_code == 200

def post_message():
    room_to_send = crpM.ChatRoomIn(name = "test_room")
    the_room = client.post('/chatroom', json = room_to_send.model_dump(mode="json"))
    room_id = the_room.json()['uid']
    to_send = crpM.MessageIn(author = "Beta_Tester", message = "ça passe ou ça casse")
    recived = client.post(f"/message/{room_id}", json = to_send.model_dump(mode="json"))
    assert recived.status_code == 200