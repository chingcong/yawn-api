#!/usr/bin/python3

from tornado.gen import coroutine
from tornado.concurrent import run_on_executor
from .handlers import BaseRequestHandler

class Main(BaseRequestHandler):

    __response = '''
        <html style="height: 100%; display: table; margin: auto; background-color: #121212;">
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body {
                        height: 100%;
                        display: table-cell;
                        vertical-align: middle;
                        color: #ffffff; 
                    }
                    h1 {
                        font-family: 'Raleway', sans-serif;
                        font-weight: 100;
                    }
                </style>
            </head>
            <body>
                <h1>
                    🥱 🌪️ 
                </h1>
            </body>
        </html>
    '''

    @coroutine
    def get(self):
        self.set_status(200)
        self.set_header('Content-Type', 'text/html; charset=UTF-8')
        self.finish(self.__response)