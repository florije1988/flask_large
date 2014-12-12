# -*- coding: utf-8 -*-
__author__ = 'florije'
from ..basic_service import BaseService
from ..models import TaskModel
from ..schemas import TaskSchema
from ..custom_exception import InvalidAPIUsage


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
        res_task = TaskModel.query().all()
        return res_task

    @staticmethod
    def get_task_by_id(task_id):
        res_task = TaskModel.query().filter(id=task_id).first()
        return res_task