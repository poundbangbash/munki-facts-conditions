import os.path

def fact():
    '''Return if InCopy 15 is installed'''
    if os.path.isfile('/Applications/Adobe InCopy 2020/Adobe InCopy 2020.app/Contents/MacOS/Adobe InCopy 2020'):
        return {'isInCopy15Installed': True}
    else:
        return {'isInCopy15Installed': False}


if __name__ == '__main__':
    print(fact())
