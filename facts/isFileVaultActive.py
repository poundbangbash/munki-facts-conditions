'''Check if FileVault is Active'''

import subprocess

def fact():
    '''Check if FileVault is Active'''
    cmd = ['/usr/bin/fdesetup', 'isactive']
    run = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = run.communicate()
    try:
        proc = subprocess.Popen(cmd, bufsize=-1, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        (out, err) = proc.communicate()

        # check if output is valid.
        if "true" in str(out):
            # Default to Des Moines location
            return {'isFileVaultActive': 'True'}
        else:
            # Return location - strip trailing newline character
            return {'isFileVaultActive': 'False'}
    except OSError:
        return {'isFileVaultActive': 'Unknown'}


if __name__ == '__main__':
    print(fact())
