from flask import Flask, request
from app.controllers import posts_controller

def routes(app: Flask):

    @app.get('/posts')
    def read_posts():
        return posts_controller.get_posts()

    @app.get('/posts/<int:id>')
    def read_post_by_id(id):
        return posts_controller.get_posts(id)

    
    @app.post('/posts')
    def create_post():
        return posts_controller.create_posts()

    
    @app.patch('/posts/<int:id>')
    def update_post(id):
        return posts_controller.updated_posts(id)

    
    @app.delete('/posts/<int:id>')
    def delete_post(id):
        return posts_controller.deleted_posts(id)