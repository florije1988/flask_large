# -*- coding: utf-8 -*-
__author__ = 'florije'
import os
from ..basic_handler import BaseHandler
from service import TaskService
from . import app_task
from flask import current_app, request
from datetime import datetime
from flask.ext.restful import reqparse
from ..custom_exception import InvalidAPIUsage


@app_task.before_app_request
def log_request_data():
    current_app.logger.warning(
        "Req----Time:~~~%r --------> remote_addr = %s, url = %s, data = %r, args = %r, values = %r" %
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), request.remote_addr, request.url,
         request.data, request.args, request.values))


class IndexHandler(BaseHandler):
    def get(self):
        return self.json_output(data={'data': 'Hello, World!'})


class FaviconHandler(BaseHandler):
    def get(self):
        # return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')
        return self.json_output(data={'pic': '/static/favicon.ico'})


class TaskHandler(BaseHandler):
    def get(self):
        # tasks = [
        #     {
        #         'id': 1,
        #         'title': u'Buy groceries',
        #         'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        #         'done': False
        #     },
        #     {
        #         'id': 2,
        #         'title': u'Learn Python',
        #         'description': u'Need to find a good Python tutorial on the web',
        #         'done': False
        #     }
        # ]
        #
        # return self.json_output(data=tasks)
        with TaskService() as task_service:
            task_service.get_task_by_id(task_id=task_id)

    def post(self):
        if not request.data:
            raise InvalidAPIUsage(message='Request data type is error!')
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help="title cannot be blank!", location='json')
        parser.add_argument('content', type=str, required=True, help="content cannot be blank!", location='json')
        args = parser.parse_args()

        with TaskService() as task_service:
            task_service.create_task(**args)



class TaskListHandler(BaseHandler):
    def get(self):
        pass