#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket,sys
import time
start_time=time.time()
messages = [ b'This is the message. ',
             b'It will be sent ',
             b'in parts.',
             ]
server_address = ('192.168.1.161', 9999)
sockets=[socket.socket(socket.AF_INET,socket.SOCK_STREAM) for i in range(10000)]
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(server_address)
print(sys.stderr,'connecting to %s port %s' % server_address)
for sock in sockets:
    sock.connect(server_address)

for message in messages:

    # Send messages on both sockets
    for s in sockets:
        print (sys.stderr, '%s: sending "%s"' % (s.getsockname(), message))
        s.send(message)

    # Read responses on both sockets
    for s in sockets:
        data = s.recv(1024)
        print (sys.stderr, '%s: received "%s"' % (s.getsockname(), data))
        if not data:
            print (sys.stderr, 'closing socket', s.getsockname())

print("\033[32;1m时间为：%s\033[0"%(time.time()-start_time))