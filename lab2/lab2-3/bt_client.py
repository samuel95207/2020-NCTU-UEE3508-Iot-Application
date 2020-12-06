#!/usr/bin/env/ python3
import bluetooth

# server address & port
bd_addr = "B8:27:EB:C5:31:82"
port = 2

# create client socket
sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )

# socket connect to server
sock.connect((bd_addr,port))

# send data to server
sock.send("0710764")

# close socket
sock.close()