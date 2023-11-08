from pydantic import BaseModel

class MessageIn(BaseModel):
    author: str
    message: str

class MessageOut(BaseModel):
    uid: str
    author: str
    message: str
    date: str
    author_profile_picture: str

class ChatRoomOut(BaseModel):
    uid: str
    name: str
    messages: list[MessageOut]

class ChatRoomIn(BaseModel):
    name: str
    # topic, avatar, tags, ??