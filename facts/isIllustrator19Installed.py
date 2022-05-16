import os.path

def fact():
    '''Return if Illustrator 19 is installed'''
    if os.path.isfile('/Applications/Adobe Illustrator CC 2015/Adobe Illustrator.app/Contents/MacOS/Adobe Illustrator'):
        return {'isIllustrator19Installed': True}
    else:
        return {'isIllustrator19Installed': False}


if __name__ == '__main__':
    print(fact())
