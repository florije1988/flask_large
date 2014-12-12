# -*- coding: utf-8 -*-
__author__ = 'florije'
from flask import Blueprint
from api.custom_api import Api

app_task = Blueprint('app_task', __name__, static_folder='static', template_folder='templates')
api_task = Api(app_task, catch_all_404s=True)

from api.app_task import views

# api_task.add_resource(views.IndexHandler, '/')
api_task.add_resource(views.FaviconHandler, '/favicon.ico')
api_task.add_resource(views.TaskHandler, '/task')
api_task.add_resource(views.TaskListHandler, '/tasks')