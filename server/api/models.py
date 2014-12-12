# -*- coding: utf-8 -*-
__author__ = 'florije'
from . import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)


class TaskModel(BaseModel):
    __tablename__ = 'tasks'

    title = db.Column(db.String(length=20), default='')
    content = db.Column(db.String(length=50), default='')

    def __init__(self, title, content):
        self.title = title
        self.content = content