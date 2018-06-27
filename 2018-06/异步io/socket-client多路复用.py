#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
HOST="localhost"
PORT=9999
client=socket.socket()
client.connect((HOST,PORT))
while True:
    msg=input(">>:")
    client.send(msg.encode("utf-8"))
    data=client.recv(1024)
    print(data)