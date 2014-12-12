# -*- coding: utf-8 -*-
__author__ = 'florije'
from api.basic_service import BaseService
from api.models import TaskModel
from api.schemas import TaskSchema
from api.custom_exception import InvalidAPIUsage


class TaskService(BaseService):
    def create_task(self, **params):
        new_task = TaskModel(title=params.get('title'), content=params.get('content'))
        self.db.add(new_task)
        self.flush()
        task_ma = TaskSchema().dump(new_task)
        if task_ma.errors:
            raise InvalidAPIUsage(message=task_ma.errors)
        return task_ma.data

    @staticmethod
    def get_tasks():
        res_task = TaskModel.query.all()
        task_ma = TaskSchema().dump(res_task, many=True)
        if task_ma.errors:
            raise InvalidAPIUsage(message=task_ma.errors)
        return task_ma.data

    @staticmethod
    def get_task_by_id(task_id):
        res_task = TaskModel.query.filter(TaskModel.id == task_id).first()
        task_ma = TaskSchema().dump(res_task)
        if task_ma.errors:
            raise InvalidAPIUsage(message=task_ma.errors)
        return task_ma.data