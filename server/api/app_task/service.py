# -*- coding: utf-8 -*-
__author__ = 'florije'
from ..basic_service import BaseService
from ..models import TaskModel


class TaskService(BaseService):
    def create_task(self, **params):
        new_task = TaskModel(title=params.get('title'), content=params.get('content'))
        self.db.add(new_task)
        self.flush()

    def get_tasks(self):
        pass

    def get_task_by_id(self, task_id):
        pass

