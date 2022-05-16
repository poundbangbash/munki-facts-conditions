
import datetime

def fact():
    '''Get the current day name'''
    try:
        now = datetime.datetime.now()
        current_hour = now.strftime("%H")
    except (IOError, OSError):
        current_hour = ""

    return {'current_hour': current_hour}

if __name__ == '__main__':
    print(fact())
