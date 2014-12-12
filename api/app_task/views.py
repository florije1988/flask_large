# -*- coding: utf-8 -*-
__author__ = 'florije'
import os
from datetime import datetime

from flask import current_app, request, send_from_directory
from flask.ext.restful import reqparse

from service import TaskService
from . import app_task
from ..basic_handler import BaseHandler
from api.custom_exception import InvalidAPIUsage


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
        # return self.json_output(data={'pic': '/static/favicon.ico'})
        return send_from_directory(os.path.join(current_app.root_path, 'static'), 'img/favicon.ico')


class TaskHandler(BaseHandler):
    def get(self):
        if not request.args:
            raise InvalidAPIUsage(message='Request data type is error!')

        parser = reqparse.RequestParser()
        parser.add_argument('task_id', type=str, required=True, help="task_id cannot be blank!", location='args')
        args = parser.parse_args()

        task_id = args.get('task_id')
        with TaskService() as task_service:
            res_task = task_service.get_task_by_id(task_id=task_id)

        if not res_task:
            # raise InvalidAPIUsage(message='task_id for {task_id} is not exist!'.format(task_id=task_id))
            return self.json_output(data={})
        return self.json_output(data=res_task)

    def post(self):
        if not request.data:
            raise InvalidAPIUsage(message='Request data type is error!')

        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help="title cannot be blank!", location='json')
        parser.add_argument('content', type=str, required=True, help="content cannot be blank!", location='json')
        args = parser.parse_args()

        with TaskService() as task_service:
            new_task = task_service.create_task(**args)

        return self.json_output(data=new_task)


class TaskListHandler(BaseHandler):
    def get(self):
        with TaskService() as task_service:
            res_task = task_service.get_tasks()

        if not res_task:
            return self.json_output(data={})
        return self.json_output(data=res_task)