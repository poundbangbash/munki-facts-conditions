import os.path

def fact():
    '''Return if Illustrator 20 is installed'''
    if os.path.isfile('/Applications/Adobe Illustrator CC 2015.3/Adobe Illustrator.app/Contents/MacOS/Adobe Illustrator'):
        return {'isIllustrator20Installed': True}
    else:
        return {'isIllustrator20Installed': False}


if __name__ == '__main__':
    print(fact())
