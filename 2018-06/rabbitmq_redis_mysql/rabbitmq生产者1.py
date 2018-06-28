#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pika
#账号密码认证，在rabbitmq中设置
credentials = pika.PlainCredentials('admin', 'admin')
#建立链接
connection=pika.BlockingConnection(pika.ConnectionParameters("192.168.1.161",5672,"/",credentials))
channel = connection.channel()
#申明queue
channel.queue_declare(queue="hello2",durable=True)
channel.basic_publish(exchange='',
                      routing_key='hello2',
                      body='hello world!',
                      properties=pika.BasicProperties(
                          delivery_mode=2,
                      )
                      )
print(" [x] Sent 'Hello World!'")
connection.close()