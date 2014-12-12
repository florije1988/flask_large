# -*- coding: utf-8 -*-
__author__ = 'florije'
from datetime import datetime
import time


DATAFORMATE = '%Y-%m-%d %H:%M:%S'


def datetime_to_timestamp(date_time):
    """
    datetime(datetime.datetime) -> timestamp(int)
    2014-10-27 16:56:11 -> 1414400171
    :param date_time:
    :return:
    """
    return int(time.mktime(date_time.timetuple()))


def datetime_str_to_timestamp(date_time_str):
    """
    datetime str(str) -> timestamp(int)
    2014-10-27 16:56:11 -> 1414400171
    :param date_time_str:
    :return:
    """
    return datetime_to_timestamp(datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S'))


def timestamp_to_datetime(time_stamp):
    """
    timestamp(int) -> datetime(datetime.datetime)
    1414400171 -> 2014-10-27 16:56:11
    :param time_stamp:
    :return:
    """
    return datetime.fromtimestamp(time_stamp)
    # return time.localtime(time_stamp)


def timestamp_to_datetime_str(time_stamp):
    """
    timestamp(int) -> datetime str(str)
    1414400171 -> 2014-10-27 16:56:11
    :param time_stamp:
    :return:
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_stamp))


def current_time_stamp():
    return int(time.time())


if __name__ == '__main__':
    now_time_stamp = int(time.time())
    print now_time_stamp, type(now_time_stamp)

    date_times = timestamp_to_datetime(now_time_stamp)
    print date_times, type(date_times)

    repeat_time_stamp = datetime_to_timestamp(date_times)
    print repeat_time_stamp, type(repeat_time_stamp)

    date_times_str = timestamp_to_datetime_str(repeat_time_stamp)
    print date_times_str, type(date_times_str)

    repeat_date_time = datetime_str_to_timestamp(date_times_str)
    print repeat_date_time, type(repeat_date_time)

    '''
    1414400171 <type 'int'>
    2014-10-27 16:56:11 <type 'datetime.datetime'>
    1414400171 <type 'int'>
    2014-10-27 16:56:11 <type 'str'>
    1414400171 <type 'int'>
    '''
