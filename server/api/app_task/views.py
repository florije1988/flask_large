# -*- coding: utf-8 -*-
__author__ = 'florije'
from ..basic_handler import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        return self.json_output(data={'data': 'Hello, World!'})


class TaskHandler(BaseHandler):
    def get(self):
        tasks = [
            {
                'id': 1,
                'title': u'Buy groceries',
                'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
                'done': False
            },
            {
                'id': 2,
                'title': u'Learn Python',
                'description': u'Need to find a good Python tutorial on the web',
                'done': False
            }
        ]

        return self.json_output(data=tasks)