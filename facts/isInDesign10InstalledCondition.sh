import os.path

def fact():
    '''Return if InDesign 10 is installed'''
    if os.path.isfile('/Applications/Adobe InDesign CC 2014/Adobe InDesign CC 2014.app/Contents/MacOS/Adobe InDesign CC 2014'):
        return {'isInDesign10Installed': True}
    else:
        return {'isInDesign10Installed': False}


if __name__ == '__main__':
    print fact()
