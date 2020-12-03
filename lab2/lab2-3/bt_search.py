#!/usr/bin/env/ python3

import bluetooth

nearby_devices = bluetooth.discover_devices()

for btaddr in nearby_devices:
    print(btaddr,end=" : ")
    print(bluetooth.lookup_name(btaddr))