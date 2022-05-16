import os.path

def fact():
    '''Return if Illustrator 22 is installed'''
    if os.path.isfile('/Applications/Adobe Illustrator CC 2018/Adobe Illustrator.app/Contents/MacOS/Adobe Illustrator'):
        return {'isIllustrator22Installed': True}
    else:
        return {'isIllustrator22Installed': False}


if __name__ == '__main__':
    print(fact())
