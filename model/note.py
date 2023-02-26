import datetime


class Note:

    def __init__(self, title, message, date_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
        self.title = title
        self.message = message
        self.date_time = date_time

    def __str__(self):
        return "{} {} {}".format(self.title, self.message, self.date_time)
