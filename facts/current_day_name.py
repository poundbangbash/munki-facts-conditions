
import datetime

def fact():
    '''Get the current day name'''
    try:
        now = datetime.datetime.now()
        dayname = now.strftime("%A")
    except (IOError, OSError):
        dayname = ""

    return {'current_day_name': dayname}

if __name__ == '__main__':
    print(fact())
