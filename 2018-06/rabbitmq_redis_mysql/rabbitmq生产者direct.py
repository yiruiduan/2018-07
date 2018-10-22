#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pika
import sys
credentials=pika.PlainCredentials("rabbit","123456")
connecttion=pika.BlockingConnection(pika.ConnectionParameters("192.168.1.190",32672,"/",credentials))
channel=connecttion.channel()
#申明exchange
channel.exchange_declare(exchange="direct_logs",exchange_type="direct",durable=True)

severity=sys.argv[1] if len(sys.argv)>1 else "error"
message = ' '.join(sys.argv[2:]) or 'error message!'
channel.basic_publish(exchange="direct_logs",
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connecttion.close()