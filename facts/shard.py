'''Return the current machine shard value.

'''

import hashlib
import objc
import os
from Foundation import NSBundle


def serial():
    '''Return the machine serial number.'''
    IOKit_bundle = NSBundle.bundleWithIdentifier_("com.apple.framework.IOKit")

    functions = [
        ("IOServiceGetMatchingService", b"II@"),
        ("IOServiceMatching", b"@*"),
        ("IORegistryEntryCreateCFProperty", b"@I@@I")
        ]
    objc.loadBundleFunctions(IOKit_bundle, globals(), functions)

    kIOMasterPortDefault = 0
    kIOPlatformSerialNumberKey = 'IOPlatformSerialNumber'
    kCFAllocatorDefault = None

    platformExpert = IOServiceGetMatchingService(
                        kIOMasterPortDefault,
                        IOServiceMatching("IOPlatformExpertDevice")
                     )
    serial = IORegistryEntryCreateCFProperty(platformExpert,
                                             kIOPlatformSerialNumberKey,
                                             kCFAllocatorDefault, 0)

    return serial


def fact():
    '''Return the machine shard value based off the serial number.'''
    if serial is None:
        return 0
    # If /usr/local/shard/production exists shard is always 100 (C-levels, never testers)
    if os.path.exists('/usr/local/shard/production'):
        shard = 100
    # If /usr/local/shard/testing exists shard is always 1 to guarantee testing
    elif os.path.exists('/usr/local/shard/testing'):
        shard = 1
    else:
        shard = int(int(hashlib.md5(serial()).hexdigest(), 16) % 100)
    # we don't want to have a zero shard
    if shard == 0:
        return {'shard': shard + 1}
    else:
        return {'shard': shard}


if __name__ == '__main__':
    print fact()
