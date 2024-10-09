#!/usr/bin/python3

import os
import simplejson
from tornado import escape
from tornado.web import RequestHandler
from concurrent.futures.thread import ThreadPoolExecutor

from errors import Errors  # Assuming Errors is imported correctly
from typing import Union, Dict
from pydantic import BaseModel
from configs import configs
from utils import JSONEncoder
import logging

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BaseRequestHandler(RequestHandler):

    executor = ThreadPoolExecutor(max_workers=configs.server.max_workers)
    encoder = JSONEncoder()

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Expose-Headers", "*")
        self.set_header("Access-Control-Allow-Credentials", "false")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.set_header('Content-Type', 'application/json')

    def response(self, status_code: int=200, data: dict=None):
        self.set_status(status_code)
        self.write({
            "item": self.encoder.encode(data)  # Use JSONEncoder for encoding
        })

    def responseItems(self, status_code: int=200, data: list=[]):
        self.set_status(status_code)
        self.write({
            "items": self.encoder.encode(data)  # Use JSONEncoder for encoding
        }) 

    def responseError(self, error: Union[BaseModel, Dict]):
        self.clear()

        if not error:
            internal_error = Errors.InternalServerError()  # Instantiate error
            self.set_status(internal_error.status)
            return self.finish(self.encoder.encode(internal_error.dict()))  # Encode to JSON

        if isinstance(error, BaseModel):
            self.set_status(error.status)
            self.finish(self.encoder.encode(error.dict()))  # Encode to JSON
        else:
            self.set_status(error.get("status", 500))
            self.finish(self.encoder.encode(error))  # Encode to JSON

    def loadRequestBody(self):
        return escape.json_decode(self.request.body) if self.request.body else {}

    def loadFormData(self):
        return {k: self.get_argument(k) for k in self.request.arguments}
