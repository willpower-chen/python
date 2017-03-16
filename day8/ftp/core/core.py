#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/
from model.server import myftp
from model.client import ftpclient
def run():
    server = myftp()
    print('server is runing ...')
    server.runserver()

def run_client():
    client = ftpclient()
    client.start()

