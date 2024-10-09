#!/usr/bin/python3

from tornado.web import url
from healthcheck import TornadoHandler

# handlers
from .main import Main
from .healthcheck import health
from .notfound import NotFound

handlers = [
    url(r'/', Main),
    url(r'/healthcheck', TornadoHandler, dict(checker=health)),
]