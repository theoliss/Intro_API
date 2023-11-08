from pydantic import BaseModel

class MessageIn(BaseModel):
    author: str
    message: str

class MessageOut(BaseModel):
    uid: str
    author: str
    message: str
    date: str

class ChatRoomOut(BaseModel):
    uid: str
    name: str
    messages: list[MessageOut]

class ChatRoomIn(BaseModel):
    name: str

class ChatRoomList(BaseModel):
    uid: str
    name: str