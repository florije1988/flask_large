# -*- coding: utf-8 -*-
__author__ = 'florije'
from . import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)


class TaskModel(BaseModel):
    __tablename__ = 'tasks'

    content = db.Column(db.String(50), default='')