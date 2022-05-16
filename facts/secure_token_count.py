'''SecureToken count'''

import subprocess


def fact():
    '''SecureToken count'''
    
    p1 = subprocess.Popen(["diskutil", "apfs", "listUsers", "/"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["awk", "/\+\-\-/ {print $2}"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p3 = subprocess.Popen(["wc", "-l"], stdin=p2.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
    p2.stdout.close() # Allow p2 to receive a SIGPIPE if p3 exits.
    output,err = p3.communicate()

    return {'secureTokenCount': int(output)}


if __name__ == '__main__':
    print(fact())
