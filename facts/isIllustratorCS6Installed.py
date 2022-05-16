import os.path

def fact():
    '''Return if Illustrator CS6 is installed'''
    if os.path.isfile('/Applications/Adobe Illustrator CS6/Adobe Illustrator.app/Contents/MacOS/Adobe Illustrator'):
        return {'isIllustratorCS6Installed': True}
    else:
        return {'isIllustratorCS6Installed': False}


if __name__ == '__main__':
    print(fact())
