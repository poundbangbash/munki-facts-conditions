import os.path

def fact():
    '''Return if InCopy 16 is installed'''
    if os.path.isfile('/Applications/Adobe InCopy 2021/Adobe InCopy 2021.app/Contents/MacOS/Adobe InCopy 2021'):
        return {'isInCopy16Installed': True}
    else:
        return {'isInCopy16Installed': False}


if __name__ == '__main__':
    print(fact())
