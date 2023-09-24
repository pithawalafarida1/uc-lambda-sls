import datetime

def FormattedDate():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d_%H.%M.%S")
    return formatted_date