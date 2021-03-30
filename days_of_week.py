class WeekDayError(Exception):
    pass
	

class Weeker:
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day not in Weeker.days:
            raise WeekDayError
        else:
            self.day = day

    def __str__(self):
        return self.day

    def add_days(self, n):
        offset = 0
        if self.day == "Mon":
            offset = 1
        elif self.day == "Tue":
            offset = 2
        elif self.day == "Wed":
            offset = 3
        elif self.day == "Thu":
            offset = 4
        elif self.day == "Fri":
            offset = 5
        elif self.day == "Sat":
            offset = 6
        elif self.day == "Sun":
            offset = 7
        
        day_lookup = ((offset + n) // 7) + ((offset + n) % 7)
        found_day = Weeker.days[day_lookup -1]
        self.day = found_day
        
        
    def subtract_days(self, n):
        offset = 0
        if self.day == "Mon":
            offset = 1
        elif self.day == "Tue":
            offset = 2
        elif self.day == "Wed":
            offset = 3
        elif self.day == "Thu":
            offset = 4
        elif self.day == "Fri":
            offset = 5
        elif self.day == "Sat":
            offset = 6
        elif self.day == "Sun":
            offset = 7
        day_lookup = ((n - offset) // 7) + ((n - offset) % 7)
        found_day = Weeker.days[day_lookup -1]
        self.day = found_day


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
