import os.path

def fact():
    '''Return if Photoshop 15 is installed'''
    if os.path.isfile('/Applications/Adobe Photoshop CC 2014/Adobe Photoshop CC 2014.app/Contents/MacOS/Adobe Photoshop CC 2014'):
        return {'isPhotoshop15Installed': True}
    else:
        return {'isPhotoshop15Installed': False}


if __name__ == '__main__':
    print(fact())
