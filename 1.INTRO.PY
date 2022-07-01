'''
NAPALM (Network Automation and Programmability Abstraction Layer with Multivendor support)
is a Python library that implements a set of functions to interact with different network device Operating Systems using a unified API.
NAPALM supports several methods to connect to the devices, to manipulate configurations or to retrieve data.
'''


print('WELCOME TO NAPALM')
from napalm import get_network_driver
import json
driver = get_network_driver('ios') #method to connect the device of cisco with ios os
my_switch = driver('192.168.122.72', 'david', 'cisco') # ip, username, password
my_switch.open() # connect to device
# those line allow us access the network device

ios_output = my_switch.get_facts() # getting the data into the var ios_output
print(ios_output) # print the output

print (json.dumps(ios_output, indent=4)) # this will print that in a readable way.

interfaces = my_switch.get_interfaces()
interfaces_ip = my_switch.get_interfaces_ip()
interfaces_counters = my_switch.get_interfaces_counters()
summarry_interfaces = interfaces + ' \n' + interfaces_ip + ' \n' + interfaces_counters
print (json.dumps(summarry_interfaces, indent=4))

my_switch.close() # disconnect from the device

