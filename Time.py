class Time:
    def __init__(self, month = 0, week = 0, day = 0, hour = 0, minute = 0, second = 0):
        self.month = int(month)
        self.week = int(week)
        self.day = int(day)
        self.hour = int(hour)
        self.minute = int(minute)
        self.second = int(second)
    def display(self):
        return ("{} months {} weeks {} days {} hours {} minutes {} seconds".format(self.month, self.week, self.day, self.hour, self.minute, self.second))