from fastapi import FastAPI
import os
import socket

app = FastAPI()


@app.get("/")
async def read_root():
    return {'message': 'Hello World!'}


@app.get('/hostname')
async def get_hostname():
    return {'hostname': socket.gethostname()}


@app.get('/author')
async def get_author():
    author = os.environ.get('AUTHOR', 'Unknown')
    return {'author': author}


@app.get('/id')
async def get_id():
    uuid = os.environ.get('UUID', 'Unknown')
    return {'id': uuid}
