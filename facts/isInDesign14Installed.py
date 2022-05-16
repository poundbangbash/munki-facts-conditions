import os.path

def fact():
    '''Return if InDesign 14 is installed'''
    if os.path.isfile('/Applications/Adobe InDesign CC 2019/Adobe InDesign CC 2019.app/Contents/MacOS/Adobe InDesign CC 2019'):
        return {'isInDesign14Installed': True}
    else:
        return {'isInDesign14Installed': False}


if __name__ == '__main__':
    print(fact())
