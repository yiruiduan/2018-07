#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pika,sys
import time
credentials=pika.PlainCredentials("rabbit","123456")
connection=pika.BlockingConnection(pika.ConnectionParameters("192.168.1.190",32672,"/",credentials))
channel=connection.channel()
channel.exchange_declare(exchange="car_check",
                        exchange_type="fanout",durable=True)

result = channel.queue_declare(exclusive=True)  # 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
queue_name = result.method.queue      #生成queuename
print("\033[31;1m%s\033[0m"%queue_name)

channel.queue_bind(exchange='car_check',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body.decode("utf-8"))


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()