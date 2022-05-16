import os.path

def fact():
    '''Return if Illustrator 21 is installed'''
    if os.path.isfile('/Applications/Adobe Illustrator CC 2017/Adobe Illustrator.app/Contents/MacOS/Adobe Illustrator'):
        return {'isIllustrator21Installed': True}
    else:
        return {'isIllustrator21Installed': False}


if __name__ == '__main__':
    print(fact())
