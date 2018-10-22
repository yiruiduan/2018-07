#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pika
import sys
#账号密码认证，在rabbitmq中设置
credentials = pika.PlainCredentials('rabbit', '123456')
#建立链接
connection=pika.BlockingConnection(pika.ConnectionParameters("192.168.1.190",32672,"/",credentials))
channel = connection.channel()
#申明queue

message="".join(sys.argv[1:]) or "error"
channel.queue_declare(queue="hello2",durable=True)
channel.basic_publish(exchange='',
                      routing_key='hello2',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,
                      )
                      )
print(" [x] Sent %s"%message)
connection.close()