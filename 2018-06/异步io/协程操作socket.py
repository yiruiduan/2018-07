#!/usr/bin/python3
# -*- coding: utf-8 -*-
from gevent import socket,monkey
import gevent
monkey.patch_all()
def server(port):
    s=socket.socket()
    s.bind(("localhost",port))
    s.listen(500)
    while True:
        conn,addr=s.accept()
        gevent.spawn(handle_request,conn)

def handle_request(conn):
    try:
        data=conn.recv(1024)
        print("recv:",data)
        conn.send(data)
        if not data:
            conn.shutdown(socket.SHUT_WR)
    except Exception as ex:
        print(ex)
    finally:
        conn.close()

if __name__=="__main__":
    server(9999)