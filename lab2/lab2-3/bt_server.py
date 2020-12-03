#!/usr/bin/env/ python3

import bluetooth

bt_server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

bd_addr = "B8:27:EB:6D:C5:C0"
port = 2

bt_server_sock.bind((bd_addr,port))
bt_server_sock.listen(4)

bt_client_sock, address = bt_server_sock.accept()

print("Accepted connection from ", address)

data = bt_client_sock.recv(1024)

print("received {}".format(data.decode()))

bt_client_sock.close()
bt_server_sock.close()