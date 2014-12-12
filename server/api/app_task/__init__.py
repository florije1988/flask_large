# -*- coding: utf-8 -*-
__author__ = 'florije'
from flask import Blueprint
from ..custom_api import Api

app_task = Blueprint('app_task', __name__)
api_task = Api(app_task, catch_all_404s=True)

from . import views

api_task.add_resource(views.IndexHandler, '/')
api_task.add_resource(views.TaskHandler, '/tasks')