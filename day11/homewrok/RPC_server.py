#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/

import pika
import time,os

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))

channel = connection.channel()
channel.queue_declare(queue='rpc_queue')



def run(cmd):
    cmd_res = os.popen(cmd).read()
    return cmd_res



def on_request(ch, method, props, body):
    # n = int(body)
    cmd = str(body)
    print(" [.] run(%s)" % cmd)
    response = run(cmd)
    print(response)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id= \
                                                         props.correlation_id), #确保发过去的是收到的。
                     # body=str(response))
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(on_request, queue='rpc_queue')
print(" [x] Awaiting RPC requests")
channel.start_consuming()