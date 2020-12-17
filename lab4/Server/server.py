import socket
import sys
import time
HOST = '192.168.0.125'
PORT = 8001

u = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print 'socket created'
try:
    u.bind((HOST,PORT))
except socket.error as err:
    print 'Bind Failed, Error Code: ' + str(err[0]) + ' , Message: ' + err[1]
    sys.exit()
print 'Socket Bind Success!'

botaddr = [0,0]

while 1:
    data,addr = u.recvfrom(1024)
    # print 'Connection with ' + addr[0] + ':' + str(addr[1])
    # print ' ' + data
    distance = 200
    if(data == 'BOT'):
        botaddr[0] = addr[0]
        botaddr[1] = addr[1]
    else:    
        distance = float((str(data)))
        print "distance: "+str(distance)
        if(botaddr[0] != 0):
            if(distance < 20):
                u.sendto('s',(botaddr[0],botaddr[1]))

    #doing something
    # distance = int((str(data)))

    
