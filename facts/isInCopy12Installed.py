import os.path

def fact():
    '''Return if InCopy 12 is installed'''
    if os.path.isfile('/Applications/Adobe InCopy CC 2017/Adobe InCopy CC 2017.app/Contents/MacOS/Adobe InCopy CC 2017'):
        return {'isInCopy12Installed': True}
    else:
        return {'isInCopy12Installed': False}


if __name__ == '__main__':
    print(fact())
