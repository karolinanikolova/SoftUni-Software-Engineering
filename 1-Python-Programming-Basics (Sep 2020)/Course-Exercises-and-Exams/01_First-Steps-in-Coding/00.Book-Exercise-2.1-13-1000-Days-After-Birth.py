# Задача: ** пресмятане с дати - 1000 дни на Земята
# Напишете програма, която въвежда рождена дата във формат dd-MM-yyyy и пресмята датата, на която се
# навършват 1000 дни от тази рождена дата и я отпечатва в същия формат.

# https://www.w3schools.com/python/python_datetime.asp
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# https://stackoverflow.com/questions/19480028/attributeerror-datetime-module-has-no-attribute-strptime

import datetime

birthday_date_string = input()

birthday_date = datetime.datetime.strptime(birthday_date_string, "%d-%m-%Y")

delta = datetime.timedelta(days=1000)

future_date = birthday_date + delta

future_date_only = datetime.datetime.date(future_date)

future_date_formatted = datetime.date.strftime(future_date_only, "%d-%m-%Y")

print(future_date_formatted)
