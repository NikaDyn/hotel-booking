from datetime import datetime


def validate_date(*args):
    for date in args:
        dates = list(map(int, date.split(".")))
        if not (0 < dates[0] < 32 and 0 < dates[1] < 13 and 2024 < dates[2]):
            return False

    return True


def check_dates(*args):
    lst_dates = []
    for date in args:
        dates = list(map(int, date.split(".")))
        date1 = datetime(dates[2], dates[1], dates[0])
        lst_dates.append(date1)

    if lst_dates[0] < lst_dates[1]:
        return False

    return True
