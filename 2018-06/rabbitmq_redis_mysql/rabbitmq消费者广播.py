#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pika,sys
import time
credentials=pika.PlainCredentials("admin","admin")
connection=pika.BlockingConnection(pika.ConnectionParameters("192.168.1.161",5672,"/",credentials))
channel=connection.channel()
channel.exchange_declare(exchange="logs",
                        exchange_type="fanout",durable=True)

result = channel.queue_declare(exclusive=True)  # 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
queue_name = result.method.queue      #生成queuename
print("\033[31;1m%s\033[0m"%queue_name)

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()