# -*- coding: utf-8 -*-
__author__ = 'florije'
from . import ma
from flask.ext.marshmallow import fields


class TaskSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'title', 'content')


class TaskListSchema(ma.Schema):
    # task_list = fields.Nested(TaskSchema)
    pass