import subprocess as sp
import sys

def login_adapters(adap_count, pass_list):
    inp = int(raw_input('enter 1 to login and '\
        'get started... '))
    
    if inp != 1:
        sys.exit('bye bye...')

    print 'now logging into the adapters... '

    visited_id = []
    num_of_ips = 0
    
    for adap_num in xrange(adap_count):
        for username in pass_list.keys():
            if username not in visited_id:
                password = pass_list[username]
                login(username, password, adap_num)
                visited_id.append(username)
                num_of_ips += 1
                break
            
    return num_of_ips
