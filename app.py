from typing import Text
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text
from datetime import datetime
from uuid import uuid4 as uid

app = FastAPI()

posts = []

class post(BaseModel):
    fecha: datetime = datetime.now()
    cliente_id: str
    descripcion: Text 
    subtotal: str
    itbis: str
    total: str


@app.get('/')
def read_root():
    return{"welcome":"hola mundo de nuevo"}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/agregar')
def gruardar_factura(post: post):
    post.id = str(uid())
    posts.append(post.dic())
    return posts[-1]


@app.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in posts:
        if post: {"id"}
    return "recibido"

@app.put("/post/{post_id}")
def editar_factura(post_id: str, updatePost: post):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts[index][cliente_id] = updatePost.cliente_id
            posts[index][descripcion] = updatePost.descripcion
            posts[index][subtotal] = updatePost.subtotal
            posts[index][itbis] = updatePost.itbis
            posts[index][total] = updatePost.total
        return "datos actualizados"





@app.delete("/posts/{post_id}")
def borrar_factura(post_id: str):
    for index,post in enumerate(posts):
      if post["id"] == post_id:
          posts.pop(index)
          return{"message":"se elimino correctamente"}
   