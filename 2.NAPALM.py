from napalm import get_network_driver

import json
driver = get_network_driver('ios') #method to connect the device of cisco with ios os
my_switch = driver('192.168.122.72', 'david', 'cisco') # ip, username, password
my_switch.open() # connect to device
# those line allow us access the network device

ios_output = my_switch.get_mac_address_table() # getting mac address table

print (json.dumps(ios_output, indent=4)) # this will print that in a readable way.

ios_output = my_switch.get_arp_table() # getting arp table
print (json.dumps(ios_output, indent=4))

result_ping = my_switch.ping('google.com')
print (json.dumps(result_ping, indent=4))

my_switch.close() # disconnect from the device