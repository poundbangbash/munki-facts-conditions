import os.path

def fact():
    '''Return if InDesign 13 is installed'''
    if os.path.isfile('/Applications/Adobe InDesign CC 2018/Adobe InDesign CC 2018.app/Contents/MacOS/Adobe InDesign CC 2018'):
        return {'isInDesign13Installed': True}
    else:
        return {'isInDesign13Installed': False}


if __name__ == '__main__':
    print(fact())
