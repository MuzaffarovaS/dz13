import datetime
date = datetime.date(2015, 6, 16)
week_number = date.isocalendar()[1]
print(week_number)