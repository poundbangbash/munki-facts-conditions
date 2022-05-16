import os.path

def fact():
    '''Return if Photoshop 21 is installed'''
    if os.path.isfile('/Applications/Adobe Photoshop 2020/Adobe Photoshop 2020.app/Contents/MacOS/Adobe Photoshop 2020'):
        return {'isPhotoshop21Installed': True}
    else:
        return {'isPhotoshop21Installed': False}


if __name__ == '__main__':
    print(fact())
