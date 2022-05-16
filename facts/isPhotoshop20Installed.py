import os.path

def fact():
    '''Return if Photoshop 20 is installed'''
    if os.path.isfile('/Applications/Adobe Photoshop CC 2019/Adobe Photoshop CC 2019.app/Contents/MacOS/Adobe Photoshop CC 2019'):
        return {'isPhotoshop20Installed': True}
    else:
        return {'isPhotoshop20Installed': False}


if __name__ == '__main__':
    print(fact())
