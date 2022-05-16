import platform
import plistlib
import subprocess
from distutils.version import LooseVersion

def get_os_version():
    '''Return OS version.'''
    return LooseVersion(platform.mac_ver()[0])

def fact():
    '''Check MDM Enrollment Status'''
    # Check the OS and run our checks based on OS version
    if get_os_version() >= LooseVersion('10.13.4'):
        # print 'Checking mdm status - modern'
        if check_mdm_status_modern():
            # print 'MDM enrolled device %s' % get_os_version()
            return {'isMDMEnrolled': True} 
    else:
        # Anything lower than 10.13.4, we just check if the profile is
        # installed
        cmd = ['/usr/bin/profiles', '-C', '-o', 'stdout-xml']
        run = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = run.communicate()
        try:
            plist = plistlib.loads(output)
        except AttributeError:
            plist = {'_computerlevel': []}
            # plistlib module doesn't have a loads function (as in Python 2)
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
                        return {'isMDMEnrolled': True}       
        except KeyError:
            return {'isMDMEnrolled': False}

    return {'isMDMEnrolled': False}

def check_mdm_status_modern():
    '''Only for 10.13.4 and higher'''
    uamdm_enrolled = 'MDM enrollment: Yes (User Approved)'

    cmd = ['/usr/bin/profiles', 'status', '-type', 'enrollment']
    run = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = run.communicate()
    mdm_status = output.decode().split('\n')[1]
    uamdm_enrollment_status = bool(uamdm_enrolled == mdm_status)
    return (uamdm_enrollment_status)

if __name__ == '__main__':
    print(fact())
