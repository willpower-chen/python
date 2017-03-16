#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/

import pymysql

# 创建连接
conn = pymysql.connect(host='192.168.52.113 ', port=3306, user='root', passwd='521013', db='cgpower_test')
# 创建游标
cursor = conn.cursor()

data = [
	('n1',22,'2016-05-21'),
	('n2',23,'2016-05-22'),
	('n3',24,'2016-05-22')
]

# 执行SQL，并返回受影响行数
cursor.executemany("insert into student(name,age,register_date)values(%s,%s,%s)", data)


# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()