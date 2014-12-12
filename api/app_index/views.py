# -*- coding: utf-8 -*-
__author__ = 'florije'
from .import app_index
from flask import render_template


@app_index.route('/')
def index():
    return render_template('index.html')