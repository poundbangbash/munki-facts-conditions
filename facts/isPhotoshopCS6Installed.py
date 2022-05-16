import os.path

def fact():
    '''Return if Photoshop CS6 is installed'''
    if os.path.isfile('/Applications/Adobe Photoshop CS6/Adobe Photoshop CS6.app/Contents/MacOS/Adobe Photoshop CS6'):
        return {'isPhotoshopCS6Installed': True}
    else:
        return {'isPhotoshopCS6Installed': False}


if __name__ == '__main__':
    print(fact())
