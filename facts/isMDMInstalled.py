'''Check MDM enrollment'''

import subprocess
import plistlib
import sys

def fact():
    '''Check MDM enrollment'''
    cmd = ['/usr/bin/profiles', '-C', '-o', 'stdout-xml']
    run = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = run.communicate()
    try:
        plist = plistlib.loads(output)
    except AttributeError:
        # plistlib module doesn't have a loads function (as in Python 2)
        plist = {'_computerlevel': []}
        try:
            plist = plistlib.readPlistFromString(output)
        except BaseException as err:
            raise PlistReadError(err)
    try:
        for possible_plist in plist['_computerlevel']:
            for item_content in possible_plist['ProfileItems']:
                try:
                    profile_type = item_content['PayloadType']
                except KeyError:
                    profile_type = ''
                if profile_type == 'com.apple.mdm':
                    return {'isMDMInstalled': True}       
    except KeyError:
        return {'isMDMInstalled': False}

    return {'isMDMInstalled': False}


if __name__ == '__main__':
    print(fact())

