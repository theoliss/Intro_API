from typing import Union
from fastapi import FastAPI

from chatroom_project.models import MessageIn, MessageOut, ChatRoomIn, ChatRoomOut

import uuid
import datetime

app = FastAPI()

@app.post("/message/{room_id}", tags=['message'])
def post_a_message(room_id: str, message: MessageIn):
    uid = uuid.uuid4()
    author = message.author
    message = message.message
    date = str(datetime.datetime.now())
    author_profile_picture = ""
    to_send = MessageOut(uid, author, message, date, author_profile_picture)
    

@app.get("/message/{room_id}", tags=['message'])
def get_messages(room_id: str) -> ChatRoomOut:
    return None #TODO code that

@app.delete("/message/{message_id}", tags=['message'])
def delete_a_message(message_id: str):
    pass #TODO code this

@app.delete("/chatroom/{room_id}", tags=['chatroom'])
def delete_chatroom(room_id: str):
    pass #TODO code this

@app.post("/chatroom", tags=['chatroom'])
def create_a_chatroom(chatroom: ChatRoomIn):
    pass


