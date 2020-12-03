#!/usr/bin/env/ python3

import bluetooth

bd_addr = "B8:27:EB:C5:31:82"

port = 2

sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr,port))

sock.send("0710764")

sock.close()