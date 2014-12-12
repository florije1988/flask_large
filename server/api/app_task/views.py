# -*- coding: utf-8 -*-
__author__ = 'florije'
import os
from ..basic_handler import BaseHandler
from service import TaskService
from . import app_task
from flask import current_app, request, send_from_directory, redirect, url_for
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


class FaviconHandler(BaseHandler):
    def get(self):
        # return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')
        return url_for('static', filename='favicon.ico')


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