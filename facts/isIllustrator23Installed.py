import os.path

def fact():
    '''Return if Illustrator 23 is installed'''
    if os.path.isfile('/Applications/Adobe Illustrator CC 2019/Adobe Illustrator.app/Contents/MacOS/Adobe Illustrator'):
        return {'isIllustrator23Installed': True}
    else:
        return {'isIllustrator23Installed': False}


if __name__ == '__main__':
    print(fact())
