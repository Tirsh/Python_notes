import datetime


def parse_date_time(date_time_str):
    return datetime.datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
