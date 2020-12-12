import socket
import sys
HOST = '192.168.50.138'
PORT = 8001

t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #TCP
print ('#Step1 < Server Start > ')
print (' socket created')
try:
    t.bind((HOST, PORT))
except socket.error as err:
    print (' Bind Failed, Error Code: ' + str(err[0]) + ', Message: ' + err[1])
    sys.exit()

print (' Socket Bind Success!')

#listen(): This method sets up and start TCP listener.
t.listen(12)
print (' Socket is now listening')

while 1:    
    print ('----')
    conn,addr = t.accept()
    buf = conn.recv(1024)
    print ('Connect with ' + addr[0] + ':' + str(addr[1]))
    print (' ' + buf)