#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/7/26 17:34
# @Author  : Willpower-chen

import os,sys,getpass

lock_file = 'lock_file.txt'
account_file = 'account_file.txt'

i = 0
while i<3:
	username = input("please enter your user name:")
	username = username.strip()
	lock_check = open(lock_file,'r+')
	f = open(account_file,'r')
	for line in lock_check.readlines():
		line = line.strip('\n')
		if username == line:
			sys.exit("User %s is locked!!!",username)

	password = input('please enter your password:')
	for a_line in f.readlines():
		user,passwd = a_line.strip('/n').split()
		if username == user and password == passwd:
			sys.exit('Welcom %s to the user platform!!! '% username)
		elif username != user:
			sys.exit("please enter the correct user name !!!")
		elif username == user and password != passwd:
			print('please enter the correct password')
			i +=1
	f.close()
else:
	print('your account %s is locked'% username)
	l = open(lock_file,'a')
	l.write(username)
	l.write('\n')
	l.close()








