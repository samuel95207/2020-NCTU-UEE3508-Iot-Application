#!/usr/bin/env/ python3
import bluetooth

# create bluetooth socket
bt_server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# address & port
bd_addr = "B8:27:EB:6D:C5:C0"
port = 2

# bind bluetooth server socket to the server's bluetooth address & port
bt_server_sock.bind((bd_addr,port))
bt_server_sock.listen(1)

# accept client connection
bt_client_sock, address = bt_server_sock.accept()
print("Accepted connection from ", address)

# receive and print data from client
data = bt_client_sock.recv(1024)
print("received {}".format(data.decode()))

# close client and server socket
bt_client_sock.close()
bt_server_sock.close()