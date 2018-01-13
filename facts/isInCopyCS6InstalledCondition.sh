import os.path

def fact():
    '''Return if InCopy CS6 is installed'''
    if os.path.isfile('/Applications/Adobe InCopy CS6/Adobe InCopy CS6.app/Contents/MacOS/Adobe InCopy CS6'):
        return {'isInCopyCS6Installed': True}
    else:
        return {'isInCopyCS6Installed': False}


if __name__ == '__main__':
    print fact()
