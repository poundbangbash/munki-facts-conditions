import os.path

def fact():
    '''Return if Illustrator 25 is installed'''
    if os.path.isfile('/Applications/Adobe Illustrator 2021/Adobe Illustrator.app/Contents/MacOS/Adobe Illustrator'):
        return {'isIllustrator25Installed': True}
    else:
        return {'isIllustrator25Installed': False}


if __name__ == '__main__':
    print(fact())
