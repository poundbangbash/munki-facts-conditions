import os.path

def fact():
    '''Return if Illustrator 18 is installed'''
    if os.path.isfile('/Applications/Adobe Illustrator CC 2014/Adobe Illustrator.app/Contents/MacOS/Adobe Illustrator'):
        return {'isIllustrator18Installed': True}
    else:
        return {'isIllustrator18Installed': False}


if __name__ == '__main__':
    print(fact())
