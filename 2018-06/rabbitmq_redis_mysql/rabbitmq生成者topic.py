#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pika,sys
credentials=pika.PlainCredentials("admin","admin")
connection=pika.BlockingConnection(pika.ConnectionParameters("192.168.1.161",5672,"/",credentials))
channel=connection.channel()
#申明exchange
channel.exchange_declare(exchange="topic_logs",exchange_type="topic",durable=True)
routing_key=sys.argv[1] if len(sys.argv)>1 else "anonymous.info"
message="".join(sys.argv[2:]) or "hello world"
channel.basic_publish(exchange="topic_logs",
                      routing_key=routing_key,
                      body=message)
connection.close()