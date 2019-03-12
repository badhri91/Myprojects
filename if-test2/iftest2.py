#!/usr/bin/env python3

ipchk=input('Apply the IP:')
        
if ipchk == '192.168.70.1':
    print('The IP address ' + ipchk + ' is same as default gateway and not recommended')
elif ipchk:
    print('Looks like the IP address was set: ' + ipchk)
else:
    print('Invalid Input Address')
