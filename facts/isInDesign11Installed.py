import os.path

def fact():
    '''Return if InDesign 11 is installed'''
    if os.path.isfile('/Applications/Adobe InDesign CC 2015/Adobe InDesign CC 2015.app/Contents/MacOS/Adobe InDesign CC 2015'):
        return {'isInDesign11Installed': True}
    else:
        return {'isInDesign11Installed': False}


if __name__ == '__main__':
    print fact()
