import os.path

def fact():
    '''Return if InDesign 16 is installed'''
    if os.path.isfile('/Applications/Adobe InDesign 2021/Adobe InDesign 2021.app/Contents/MacOS/Adobe InDesign 2021'):
        return {'isInDesign16Installed': True}
    else:
        return {'isInDesign16Installed': False}


if __name__ == '__main__':
    print(fact())
