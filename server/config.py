# -*- coding: utf-8 -*-
__author__ = 'florije'
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    TESTING = False

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_TIMEOUT = 10
    SQLALCHEMY_POOL_RECYCLE = 7200
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    APP_DEBUG = True
    HOST = 'localhost'
    PORT = 5000
    LOG_PATH = 'lukker_logs'
    LOG_NAME = 'lukker_logs.log'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:903326@localhost/lukker'


class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    # 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    SQLALCHEMY_DATABASE_URI = 'mysql://root:903326@localhost/sns_florije'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}