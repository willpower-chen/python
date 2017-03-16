#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/
'''
变量配置
'''

main_menu = ['\033[36;1m查询\033[0m', \
			 '\033[35;1m添加修改\033[0m',\
			 '\033[34;1m删除\033[0m', \
			 '\033[33;1m确认修改并备份\033[0m',\
			 '\033[32;1m显示backend完整信息\033[0m']
haproxy_file = "haproxy.conf"
indentation = 4
record_op_list = ['server','weight', 'maxconn']
record_op = {'server':"", 'weight':0 , 'maxconn':0}

