from typing import Union
from fastapi import FastAPI, HTTPException
import os.path

if os.path.isfile('models.py'):
    from models import MessageIn, MessageOut, ChatRoomIn, ChatRoomOut, ChatRoomInfo
else :
    from chatroom_project.models import MessageIn, MessageOut, ChatRoomIn, ChatRoomOut, ChatRoomInfo

import uuid
from datetime import datetime

app = FastAPI()




class Message:
    def __init__(self, author: str, message):
        self.author = author
        self.message = message
        self.uid = str(uuid.uuid4())
        self.date = datetime.now()
class Chatroom:
    def __init__(self, name: str):
        self.uid = str(uuid.uuid4())
        self.name = name
        self.messages = list[Message]
        
chatrooms: dict[str : Chatroom] = {}

@app.post("/message/{room_id}", tags=['message'])
def post_a_message(room_id: str, message: MessageIn):
    if room_id not in chatrooms:
        raise HTTPException(status_code=404, detail="Chatroom not found")
    msg = Message(message.author, message.message)
    chatrooms[room_id].messages.append(msg)
    return "Message successfully sent!"
    

@app.get("/message/{room_id}", tags=['message'])
def get_messages(room_id: str) -> ChatRoomOut:
    room = chatrooms[room_id]
    return ChatRoomOut(uid= room_id, name= room.name, messages= room.messages)

@app.delete("/message/{message_id}", tags=['message'])
def delete_a_message(message_id: str):
    pass #TODO code this

@app.delete("/chatroom/{room_id}", tags=['chatroom'])
def delete_chatroom(room_id: str):
    if room_id not in chatrooms:
        raise HTTPException(status_code=404, detail="Chatroom not found")
    
@app.get("/chatroom", tags=['chatroom'])
def get_chatrooms() -> list[ChatRoomInfo]:
    chat_list = []
    for room in chatrooms.values():
        chat_list.append(ChatRoomInfo(uid= room.uid, name= room.name))
    return chat_list

@app.post("/chatroom", tags=['chatroom'])
def create_a_chatroom(chatroom: ChatRoomIn):
    room = Chatroom(chatroom.name)
    chatrooms[room.uid] = room
    return ChatRoomInfo(uid= room.uid, name= room.name)


