# -*- coding: utf-8 -*-
__author__ = 'florije'
from ..basic_handler import BaseHandler
from service import TaskService
from . import app_task
from flask import current_app, request
from datetime import datetime


@app_task.before_app_request
def log_request_data():
    current_app.logger.warning(
        "Req----Time:~~~%r --------> remote_addr = %s, url = %s, data = %r, args = %r, values = %r" %
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), request.remote_addr, request.url,
         request.data, request.args, request.values))


class IndexHandler(BaseHandler):
    def get(self):
        return self.json_output(data={'data': 'Hello, World!'})


class InitDBHandler(BaseHandler):
    def get(self):
        with TaskService() as task_service:
            res = task_service.init()
        return self.json_output(data={'db': res})


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