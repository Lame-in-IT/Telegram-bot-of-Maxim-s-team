from datetime import datetime
from datetime import date, timedelta

def get_date_now():
    return "{:%Y-%m-%d}".format(datetime.now())

def get_list_date_7():
    corrent_date = "{:%Y-%m-%d}".format(datetime.now())
    format_date = corrent_date.split("-")
    year = int(format_date[0])
    month = int(format_date[1])
    day = int(format_date[2])
    first_date = date(year, month, day)
    duration = timedelta(days=7)
    list_last_day = []
    for d in range(duration.days + 1):
        day = first_date - timedelta(days=d)
        list_last_day.append(day)
    return[list_last_day[0], list_last_day[1],
          list_last_day[2], list_last_day[3],
          list_last_day[4], list_last_day[5],
          list_last_day[6], list_last_day[7]]

def get_date_7():
    corrent_date = "{:%Y-%m-%d}".format(datetime.now())
    format_date = corrent_date.split("-")
    year = int(format_date[0])
    month = int(format_date[1])
    day = int(format_date[2])
    first_date = date(year, month, day)
    duration = timedelta(days=7)
    list_last_day = []
    for d in range(duration.days + 1):
        day = first_date - timedelta(days=d)
        list_last_day.append(day)
    return list_last_day[7]

def gey_list_date_365():
    corrent_date_1 = "{:%Y, %m, %d}".format(datetime.now())
    format_date = corrent_date_1.split(",")
    year = int(format_date[0])
    month = int(format_date[1])
    day = int(format_date[2])
    first_date = date(year, month, day)
    duration_1 = timedelta(days=365)
    list_last_day_31 = []
    for d_1 in range(duration_1.days + 1):
        day_1 = first_date - timedelta(days=d_1)
        list_last_day_31.append(day_1)
    return list_last_day_31[365]

if __name__=="__main__":
    get_date_now()