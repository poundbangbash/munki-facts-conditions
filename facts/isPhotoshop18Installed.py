import os.path

def fact():
    '''Return if Photoshop 18 is installed'''
    if os.path.isfile('/Applications/Adobe Photoshop CC 2017/Adobe Photoshop CC 2017.app/Contents/MacOS/Adobe Photoshop CC 2017'):
        return {'isPhotoshop18Installed': True}
    else:
        return {'isPhotoshop18Installed': False}


if __name__ == '__main__':
    print(fact())
