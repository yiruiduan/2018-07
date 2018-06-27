#!/usr/bin/python3
# -*- coding: utf-8 -*-
import selectors,socket
HOST="localhost"
PORT=9999
sel=selectors.DefaultSelector()

def accept(server,mask):
    conn,addr=server.accept()
    print("accepted",conn,"from",addr)
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,read)

def read(conn,mask):
    data=conn.recv(1024)
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

server=socket.socket()
server.bind((HOST,PORT))
server.listen(100)
server.setblocking(False)
sel.register(server,selectors.EVENT_READ,accept)

while True:
    events = sel.select()
    # print("\033[31;1m%s\033[0m"%events)
    for key,mask in events:
        callback = key.data
        print("\033[31;1m%s\033[0m"%callback)
        callback(key.fileobj, mask)