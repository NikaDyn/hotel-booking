from datetime import datetime


def validate_date(date: str):
    if date.count(".") != 2:
        return False

    parts = date.split(".")
    if not all(part.isdigit() for part in parts):
        return False

    day, month, year = map(int, parts)
    if not (1 <= day <= 31 and 1 <= month <= 12 and year >= 2025):
        return False

    if month == 2 and day > 29:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False

    return True


def check_dates(date1: str, date2: str):
    d1 = list(map(int, date1.split(".")))
    d2 = list(map(int, date2.split(".")))

    dt1 = datetime(d1[2], d1[1], d1[0])
    dt2 = datetime(d2[2], d2[1], d2[0])

    return dt1 <= dt2


def validate_phone(phone_number: str):
    if phone_number.isdigit() and len(phone_number) == 10:
        return True

    return False
