import os.path

def fact():
    '''Return if InCopy 10 is installed'''
    if os.path.isfile('/Applications/Adobe InCopy CC 2014/Adobe InCopy CC 2014.app/Contents/MacOS/Adobe InCopy CC 2014'):
        return {'isInCopy10Installed': True}
    else:
        return {'isInCopy10Installed': False}


if __name__ == '__main__':
    print(fact())
