#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pika,sys
import time
credentials=pika.PlainCredentials("rabbit","123456")
connection=pika.BlockingConnection(pika.ConnectionParameters("192.168.1.190",32672,"/",credentials))
channel=connection.channel()
#申明exchange
channel.exchange_declare(exchange="car_check",
                        exchange_type="fanout",durable=True)

message = ' '.join(sys.argv[1:]) or "这是什么情况"
channel.basic_publish(exchange='car_check',
                      routing_key='',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=1,
                      )
                      )
print(" [x] Sent 'Hello World!'")
connection.close()