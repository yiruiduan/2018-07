#!/usr/bin/python3
# -*- coding: utf-8 -*-
import select
import socket
import sys
import queue
#在非阻塞的模式下才能实现多路复用

server=socket.socket()
server.bind(("localhost",9999))
server.listen(1000)

server.setblocking(False)#设置为非阻塞
msg_dic={}
inputs=[server]
outputs=[]
while True:
    readable,writeable,exceptional=select.select(inputs,outputs,inputs)
    print(readable,writeable,exceptional)
    for r in readable:
        if r is server:
            conn,addr=server.accept()
            print("\033[32;m有新链接：\033[0m",addr)
            inputs.append(conn)
            msg_dic[conn]=queue.Queue()#初始化一个队列，后面要存返回conn的数据
        else:
            data=r.recv(1024)
            if data:
                print(data)
                msg_dic[r].put(data)
                outputs.append(r)#放入返回的链接队列里
            else:
                print("closing",addr,"after reading no data!!!!")
                if r in outputs:
                    outputs.remove(r)
                inputs.remove(r)
                server.close()
                del msg_dic[r]

    for w in writeable:
        data_to_client=msg_dic[w].get()
        print(data_to_client)
        w.send(data_to_client)
        outputs.remove(w)

    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        del msg_dic[e]


