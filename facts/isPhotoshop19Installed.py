import os.path

def fact():
    '''Return if Photoshop 19 is installed'''
    if os.path.isfile('/Applications/Adobe Photoshop CC 2018/Adobe Photoshop CC 2018.app/Contents/MacOS/Adobe Photoshop CC 2018'):
        return {'isPhotoshop19Installed': True}
    else:
        return {'isPhotoshop19Installed': False}


if __name__ == '__main__':
    print fact()
