import imp
import json
from napalm import get_network_driver


router_list = ['17.1.1.1', '17.1.1.2', '16.8.8.2', '15.1.1.2']

for ip_address in router_list:
    print (f'connecting to {ip_address}')
    driver = get_network_driver('ios')
    ios_router = driver(ip_address, 'david', 'cisco92875i')
    ios_router.open()
    bgp_neighbors = ios_router.get_bgp_neighbors()
    print(json.dumps(bgp_neighbors, ident=4))
    ios_router.close()
    
    