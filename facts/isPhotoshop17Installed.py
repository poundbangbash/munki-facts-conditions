import os.path

def fact():
    '''Return if Photoshop 17 is installed'''
    if os.path.isfile('/Applications/Adobe Photoshop CC 2015.5/Adobe Photoshop CC 2015.5.app/Contents/MacOS/Adobe Photoshop CC 2015.5'):
        return {'isPhotoshop17Installed': True}
    else:
        return {'isPhotoshop17Installed': False}


if __name__ == '__main__':
    print fact()
