#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
def hand_request(client):
    data=client.recv(1024)
    client.send(b"HTTP/1.1 ok\r\n\r\n")
    client.send(b"hello,seven")

def main():
    socket_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_server.bind(("localhost",8000))
    socket_server.listen(5)
    while True:
        conn,addr=socket_server.accept()
        hand_request(conn)
        conn.close()


if __name__ =="__main__":
    main()
