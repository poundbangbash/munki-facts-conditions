import os.path

def fact():
    '''Return if InDesign CS6 is installed'''
    if os.path.isfile('/Applications/Adobe InDesign CS6/Adobe InDesign CS6.app/Contents/MacOS/Adobe InDesign CS6'):
        return {'isInDesignCS6Installed': True}
    else:
        return {'isInDesignCS6Installed': False}


if __name__ == '__main__':
    print fact()
