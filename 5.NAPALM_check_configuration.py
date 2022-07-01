import json
from napalm import get_network_driver


driver = get_network_driver('ios') # determite vendor device
device = driver('192.168.10.10', 'david', 'cisco') # determine ip+username+pwd
device.open() # open connection with the device

print ('connecting 192.168.10.10') 
device.load_merge_candidate(filename='new_good_configuration.txt') # load configuration file

diffrent = device.compare_config()
if len(diffrent) > 0: # check if the configuration is diffrent.
    print('the configuration is diffrent\n recharge the configuration!!!!')
    device.commit_config() # commit the configuration
else:
    print('the configuration is the same\nno changes required!!!')
    
device.close() # closing the connection with the device