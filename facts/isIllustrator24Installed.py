import os.path

def fact():
    '''Return if Illustrator 24 is installed'''
    if os.path.isfile('/Applications/Adobe Illustrator 2020/Adobe Illustrator.app/Contents/MacOS/Adobe Illustrator'):
        return {'isIllustrator24Installed': True}
    else:
        return {'isIllustrator24Installed': False}


if __name__ == '__main__':
    print(fact())
