# -*- coding: utf-8 -*-
__author__ = 'florije'
from ..basic_handler import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        return self.json_output(data={'data': 'Hello, World!'})