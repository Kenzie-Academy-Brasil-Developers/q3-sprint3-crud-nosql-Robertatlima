from flask import request, jsonify
from datetime import datetime
from http import HTTPStatus
from app.models.posts_models import Posts

def get_posts(id: int = None):
        all_posts = list(Posts.get_posts(id))
        Posts.serialize_posts(all_posts)
        if id and not all_posts:
           return {"msg": "Id não encontrado"}, HTTPStatus.NOT_FOUND
        else:
            return jsonify(all_posts), HTTPStatus.OK

def create_posts():
    try:
        data = request.get_json()
        if False in [bool(value) for value in data.values()]:
            return {"msg": "Preencha as chaves corretamente"}, HTTPStatus.BAD_REQUEST

        create_post = Posts(**data)
        create_post.post_posts()
        Posts.serialize_posts(create_post)

        return jsonify(create_post.__dict__), HTTPStatus.CREATED

    except KeyError as key:
        return {"É necessário preencher a chave": key.args}, HTTPStatus.BAD_REQUEST


def updated_posts(id: int) -> any:

        data = request.get_json()
        upd_post = list(Posts.get_posts(id))
        Posts.serialize_posts(upd_post)
        return jsonify(upd_post), HTTPStatus.OK



def deleted_posts(id: int):
    try:
        dlt_post = Posts.delete_posts(id)
        if not dlt_post:
            raise TypeError
        Posts.serialize_posts(dlt_post)

        return jsonify(dlt_post), HTTPStatus.OK
    except TypeError:
        return {"msg": "Id não encontrado"}, HTTPStatus.NOT_FOUND