#!/usr/bin/env python3
"""
Generate networking files for Raspberry Pi
usage: python networking.py address [netmask] network broadcast gateway

"""
import json
from string import Template
import sys


def load_config():
    """
    Load the configuration file into memory.
    :rtype: dict
    """
    with open('data/config.json', 'r') as f:
        return json.load(f)


def generate_interfaces(address, netmask, network, broadcast, gateway):
    """
    Generate the interfaces file to be deployed on the server.
    :param address: Desired IP address
    :param netmask: The mask that determines what subnet an IP address belongs
                    to
    :param network: Destination IP address
    :param broadcast: Broadcast range
    :param gateway: The address of the router
    """
    args = locals()
    keys = ('ssid', 'psk')
    config = load_config()
    with open('data/interfaces-static.in', 'r') as f:
        src = Template(f.read())

    data = {key: config[key] for key in keys}
    for arg, value in args.iteritems():
        data[arg] = value

    print(src.substitute(data))


if __name__ == '__main__':
    if len(sys.argv) == 5:
        address, network, broadcast, gateway = sys.argv[1:]
        netmask = '255.255.255.0'
    elif len(sys.argv) == 6:
        address, netmask, network, broadcast, gateway = sys.argv[1:]
    else:
        print('usage: python networking.py address [netmask] network broadcast'
              ' gateway')
        sys.exit(1)

    generate_interfaces(address, netmask, network, broadcast, gateway)
