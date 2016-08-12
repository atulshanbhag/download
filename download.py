import subprocess as sp
import sys
from clear import *
from constants import *
from create_adapters import *
from load_passwords import *
from login import *
from login_adapters import *
                

def download():
    clear()
    inp = int(raw_input('enter 1 for downloading... '))
    
    if inp != 1:
        sys.exit('bye bye...')
    
    inp = int(raw_input('let\'s start downloading...\n' \
                        'enter 1 to create adapters...\n' \
                        'enter 2 to skip creating adapters ' \
                        'and start downloading... '))
                        
    if inp == 1:
        CREATE_ADAPTERS = True
        START_DOWNLOAD = True
    elif inp == 2:
        CREATE_ADAPTERS = False
        START_DOWNLOAD = True

    if not CREATE_ADAPTERS and not START_DOWNLOAD:
        sys.exit('bye bye...')

    if CREATE_ADAPTERS:
        pass_list = load_passwords()
        adap_count = create_adapters()
        num_of_ips = login_adapters(adap_count, pass_list)

        if num_of_ips < adap_count:
            print 'not all IDs could login... some IDs may be' \
                ' not matching, or data must have exceeded...'
        else:
            print 'all IDs were logged in on the adapters...'

    