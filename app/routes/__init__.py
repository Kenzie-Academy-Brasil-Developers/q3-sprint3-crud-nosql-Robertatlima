
from flask import Flask


def init_app(app):
    from app.routes.home_route import routes
    routes(app)