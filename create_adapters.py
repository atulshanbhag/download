import subprocess as sp
from clear import clear
from constants import *


def create_adapters():
    adap_count = int(raw_input('enter number of ' \
        'adapters to create... '))
    adap_count = min(adap_count, MAX_ADAPCOUNT)
    
    print 'creating %d adapters now...' % adap_count
    ipstart = IPSTART
        
    for i in xrange(ipstart, ipstart + adap_count):
        cmd = 'sudo ifconfig "eth1:%d" "%s%d" ' \
            'netmask %s broadcast %s up' % \
            (i - IPSTART, ROOT_HOSTEL_IP, i, 
             NETMASK_IP, BROADCAST_IP)
        sp.Popen(cmd, shell=True, stdout=sp.PIPE)
        
    clear()
    print 'adapters have been successfully created...'
    return adap_count
