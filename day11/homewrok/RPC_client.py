#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/

import pika
import uuid
import time

class SshRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, #只要已收到消息就调用on_response
                                   no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                   ),
                                   body=str(n))

        while self.response is None:
            self.connection.process_data_events() #非阻塞版的start_consuming()
            print("no msg.....")
            time.sleep(0.5)
        return int(self.response)

while True:
    cmd = input(">>:").strip()
    if cmd == ("quit" and "exit") :
        break
    else:
        ssh_rpc = SshRpcClient()
        print(" [x] Requesting run(%s)"%cmd)
        # cmd_res = int(cmd)
        response = ssh_rpc.call(cmd)
        print(" [.] Got %r" % response)