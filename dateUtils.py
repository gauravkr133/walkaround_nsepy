from datetime import datetime


def getDate(date_str):
    return datetime.strptime(date_str, '%d-%m-%Y').date()
