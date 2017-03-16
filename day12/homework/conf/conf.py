#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/
WELCOME_MSG = '''------------------ 欢迎光临学员管理系统 ------------------'''
ERRORNO = {
    '1001' : 'Auth fail: wrong username or password',
    '1002' : 'Too many attempts',
    '2001' : 'Command [%s] is not exist!',
    '2002' : 'invalid option !',
    '3001' : 'Invalid usage, Usage(s): %s',
    '4001' : 'File %s is not exist!',
    '5001' : 'Connect fail!',
}
DBS = {"real" : "mysql+pymysql://root:521013@192.168.52.113/cgpower_test", # 正式环境数据库
       }

DB = DBS['real']