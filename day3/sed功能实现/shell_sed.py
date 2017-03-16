#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/
'''
sed替换功能
'''

import os,sys
find_str = sys.argv[1]	#要替换的内容
replace_str = sys.argv[2]	#替换后的内容

with open('file.txt','r',encoding='utf-8') as read_line,\
	  open('newfile.txt','w',encoding='utf-8') as write_line:
	for line in read_line:
		if find_str in line:
			line = line.replace(find_str,replace_str)
		write_line.write(line)
if os.path.exists('file.txt.bak'):#判断.bak文件存在的话，删除
	os.remove('file.txt.bak')
os.rename('file.txt','file.txt.bak')#原文件做备份
os.rename('newfile.txt','file.txt')#新文件替换



