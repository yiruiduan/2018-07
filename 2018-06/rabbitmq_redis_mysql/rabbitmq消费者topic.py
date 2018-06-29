#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pika
import sys
credentials=pika.PlainCredentials("admin","admin")
connection=pika.BlockingConnection(pika.ConnectionParameters("192.168.1.147",5672,"/",credentials))
channel=connection.channel()
#申明exchange
channel.exchange_declare(exchange="topic_logs",exchange_type="topic",durable=True)
#创建临时queue
result=channel.queue_declare(exclusive=True)
queue_name=result.method.queue

binding_keys=sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange="topic_logs",
                       routing_key=binding_key,
                       queue=queue_name)
print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()