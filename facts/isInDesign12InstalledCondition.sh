import os.path

def fact():
    '''Return if InDesign 12 is installed'''
    if os.path.isfile('/Applications/Adobe InDesign CC 2017/Adobe InDesign CC 2017.app/Contents/MacOS/Adobe InDesign CC 2017'):
        return {'isInDesign12Installed': True}
    else:
        return {'isInDesign12Installed': False}


if __name__ == '__main__':
    print fact()
