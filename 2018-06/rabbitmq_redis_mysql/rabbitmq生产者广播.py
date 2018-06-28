#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pika,sys
import time
credentials=pika.PlainCredentials("admin","admin")
connection=pika.BlockingConnection(pika.ConnectionParameters("192.168.1.161",5672,"/",credentials))
channel=connection.channel()
#申明exchange
channel.exchange_declare(exchange="logs",
                        exchange_type="fanout",durable=True)

message = ' '.join(sys.argv[1:]) or "where!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,
                      )
                      )
print(" [x] Sent 'Hello World!'")
connection.close()