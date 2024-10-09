#!/usr/bin/python3

from .handlers import BaseRequestHandler

class NotFound(BaseRequestHandler):

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
                    👀
                </h1>
            </body>
        </html>
    '''
    
    def prepare(self):
        self.set_status(404)
        self.set_header('Content-Type', 'text/html; charset=UTF-8')
        self.finish(self.__response)