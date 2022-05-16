import os.path

def fact():
    '''Return if InCopy 11 is installed'''
    if os.path.isfile('/Applications/Adobe InCopy CC 2015/Adobe InCopy CC 2015.app/Contents/MacOS/Adobe InCopy CC 2015'):
        return {'isInCopy11Installed': True}
    else:
        return {'isInCopy11Installed': False}


if __name__ == '__main__':
    print(fact())
