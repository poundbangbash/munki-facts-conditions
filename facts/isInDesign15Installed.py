import os.path

def fact():
    '''Return if InDesign 15 is installed'''
    if os.path.isfile('/Applications/Adobe InDesign 2020/Adobe InDesign 2020.app/Contents/MacOS/Adobe InDesign 2020'):
        return {'isInDesign15Installed': True}
    else:
        return {'isInDesign15Installed': False}


if __name__ == '__main__':
    print(fact())
