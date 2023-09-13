import datetime

def format_datetime(dt, time=True):
    """ Transforms a datetime to be in dd-mm-yyyy (or dd-mm-yyyy_hourmin) format    """
    if (time):
        return dt.strftime('%m-%d-%Y_%H%M')
    else:
        return dt.strftime('%m-%d-%Y')