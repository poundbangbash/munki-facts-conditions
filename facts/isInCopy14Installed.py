import os.path

def fact():
    '''Return if InCopy 14 is installed'''
    if os.path.isfile('/Applications/Adobe InCopy CC 2019/Adobe InCopy CC 2019.app/Contents/MacOS/Adobe InCopy CC 2019'):
        return {'isInCopy14Installed': True}
    else:
        return {'isInCopy14Installed': False}


if __name__ == '__main__':
    print(fact())
