import os.path

def fact():
    '''Return if Photoshop 16 is installed'''
    if os.path.isfile('/Applications/Adobe Photoshop CC 2015/Adobe Photoshop CC 2015.app/Contents/MacOS/Adobe Photoshop CC 2015'):
        return {'isPhotoshop16Installed': True}
    else:
        return {'isPhotoshop16Installed': False}


if __name__ == '__main__':
    print fact()
