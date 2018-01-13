'''Get the current logged in user'''

import subprocess
from SystemConfiguration import SCDynamicStoreCopyConsoleUser
import sys

def fact():
    '''Get the current logged in user'''
    try:
    	username = (SCDynamicStoreCopyConsoleUser(None, None, None) or [None])[0]
    	username = [username,""][username in [u"loginwindow", None, u""]]
    except (IOError, OSError):
        pass

    if username == '':
    	return {'isUserLoggedIn': False}
    else:
    	return {'isUserLoggedIn': True}
