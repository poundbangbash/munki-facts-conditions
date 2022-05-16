import os.path

def fact():
    '''Return if Photoshop 22 is installed'''
    if os.path.isfile('/Applications/Adobe Photoshop 2021/Adobe Photoshop 2021.app/Contents/MacOS/Adobe Photoshop 2021'):
        return {'isPhotoshop22Installed': True}
    else:
        return {'isPhotoshop22Installed': False}


if __name__ == '__main__':
    print(fact())
