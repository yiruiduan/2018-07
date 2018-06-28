#!/usr/bin/python3
# -*- coding: utf-8 -*-
import selectors,socket
HOST="0.0.0.0"
PORT=9999
socket_server=socket.socket()
socket_server.bind((HOST,PORT))
socket_server.listen(100)
socket_server.setblocking(False)
sel=selectors.DefaultSelector()
def accept(socket_server,mask):
    conn,addr=socket_server.accept()
    sel.register(conn,selectors.EVENT_READ,read)
    conn.setblocking(False)
    # sel.select()
def read(conn,mask):
    data=conn.recv(1024)
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


sel.register(socket_server,selectors.EVENT_READ,accept)
while True:
    events=sel.select()
    print("\033[31;1m%s\033[0m"%events)
    for key,mask in events:
        call_back=key.data
        call_back(key.fileobj,mask)