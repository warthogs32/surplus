import time
from datetime import datetime
import pandas as pd
class Time:
    def __init__(self, day = 0, hour = 0, minute = 0, second = 0):
        self.day = int(day)
        self.hour = int(hour)
        self.minute = int(minute)
        self.second = int(second)
    def display(self):
        return ("{} days {} hours {} minutes {} seconds".format(self.day, self.hour, self.minute, self.second))
    def toSeconds(self):
        return self.second + self.minute*60 + self.hour*3600 + self.day*3600*24
    def toEndDateStamp(self):
        endDate = time.time() + self.toSeconds() - 25200
        return datetime.utcfromtimestamp(endDate).strftime('%d%m%Y %H:%M')