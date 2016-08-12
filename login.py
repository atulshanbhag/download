import subprocess as sp
from constants import *

def login(username, password, adap_num):
    temp_cmd = 'mode=191&userName=%s&password=%s' \
                '&password=%s&btnSubmit=Login' \
                % (username, password)
    cmd = 'curl -k -s -d "%s" %s --interface ' \
    'eth1:%d' % (temp_cmd, LOGIN_URL, adap_num)
    
    output = sp.check_output(cmd, shell=True)
    if output.find('logged in', 0, len(output)) > -1:
        print 'logged in on eth1:%d using ' \
        'ID = %s...' % (adap_num, username)
        return True
    else:
        return False 