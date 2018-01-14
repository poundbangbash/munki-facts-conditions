import os.path

def fact():
    '''Return if InCopy 13 is installed'''
    if os.path.isfile('/Applications/Adobe InCopy CC 2018/Adobe InCopy CC 2018.app/Contents/MacOS/Adobe InCopy CC 2018'):
        return {'isInCopy13Installed': True}
    else:
        return {'isInCopy13Installed': False}


if __name__ == '__main__':
    print fact()
