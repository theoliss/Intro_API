FROM python:3.10 

WORKDIR /project

ADD . .
RUN pip3 install -r requirements.txt


ENTRYPOINT [ "uvicorn", "chatroom_project.api:app", "--host", "0.0.0.0" ]