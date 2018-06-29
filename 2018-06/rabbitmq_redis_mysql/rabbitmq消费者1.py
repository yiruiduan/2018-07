#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pika
import time
#普通认证证书
cerdentials=pika.PlainCredentials("admin","admin")
connection=pika.BlockingConnection(pika.ConnectionParameters("192.168.1.147",5672,"/",cerdentials))
channel=connection.channel()
#申明使用的队列
#You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
#was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
channel.queue_declare(queue="hello",durable=True)

def callback(ch, method, properties, body):   #回调函数
    # print("============>",ch,"\n",method,"\n",properties)
    # time.sleep(3)
    print("[x] received %r"%body.decode("utf-8"))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)    #消息的分配，实现负载均衡

channel.basic_consume(#消费消息
                    callback,#如果收到消息，交给callback处理消息
                    queue='hello')
                    # no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
