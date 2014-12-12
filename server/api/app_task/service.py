# -*- coding: utf-8 -*-
__author__ = 'florije'
from ..basic_service import BaseService


class TaskService(BaseService):
    def init(self):
        self.init_db()
        return True

    def create_task(self, **params):
        pass

    def get_tasks(self):
        pass

    def get_task_by_id(self, task_id):
        pass

