#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
'''
购物商城
'''

import os,sys,codecs,time

# 将文件转为字典
def getdic(file):
	'''
	将文件转为字典
	:param file: 读取的文件
	:return: 字典
	'''
	if os.path.exists(file):
		dic = {}
		with codecs.open(file, 'r', encoding='utf-8') as f:
			for line in f.readlines():
				line = line.strip().split()
				dic[line[0]] = line[1:]
			return dic
	else:
		print('Error: file "%s" is not exist, please check!' % file)
		exit(1)
# 将文件转为列表
def getlist(file):
	'''
	# 将文件转为列表
	:param file: 读取的文件
	:return: 列表
	'''
	if os.path.exists(file):
		li = []
		with codecs.open(file, 'r', encoding='utf-8') as  f:
			for line in f.readlines():
				li.append(line.strip().split())
		return li
	else:
		print('Error: file "%s" is not exist, please check!' % file)
		exit(1)
# 将字典写入文件
def dic_to_file(file, dic):
	'''
	# 将字典写入文件
	:param file: 写入文件
	:param dic: 被导入的字典
	:return:
	'''
	with open(file, 'a', encoding='utf-8') as f:
		for key, val in dic.items():
			line = []
			line.append(key)
			line.extend(val)
			f.write(line)
# 将列表写入文件
def list_to_file(file, li):
	'''
	将列表写入文件
	:param file:
	:param li:
	:return:
	'''
	with open(file, 'a', encoding='utf-8') as f:
		for line in li:
			f.write(' '.join(line) + '\n')
#将字符写入文件
def str_to_file(file,salary):
	'''
	将字符写入文件
	:param file:
	:param salary:
	:return:
	'''
	with open(file,'w',encoding='utf-8') as f:
		f.write(str(salary))



# 如果balance.txt有工资记录，直接读取工资，如果没有就请用户输入工资，
with open('balance.txt','r',encoding='utf-8') as f:
	salary = f.read()
if len(salary) == 0: #如果salary为空，输入工资
	salary = input("Input your salary:")
	if salary.isdigit(): #如果输入的工资是数字
		salary = int(salary)
	else: #如果输入的工资不是数字，退出
		exit("Invaild data type...")
else:#如果文件中已经存有工资，字符转换为整数
	salary = int(salary)

#打印现有工资数
print('\033[31m您现在有工资%d元\033[0m'.center(100,'$')%salary)

# 打印欢迎信息
welcome_msg = '\033[33m欢迎来到本商场\033[0m'.center(100, '-')
print(welcome_msg)

# 设置标志位
exit_flag = False
#申明一个空的购物车
shop_car = []

# 读取文件中商品至列表
product_list = getlist('goods.db')
while not exit_flag:
	print("商品列表".center(100, '#'))
	for item in enumerate(product_list):		#遍历商品列表，并给商品打上标签
		index = item[0]							#商品编号
		p_name = item[1][0]						#商品名
		p_price = int(item[1][1])				#商品价格
		print(index, ' ', p_name, p_price)		#打印商品

#用户操作选择
	user_choice = input("[\033[31mq退出\033[0m,\033[32mc查看已购商品\033[0m，\033[33m数字购买商品\033[0m]，请选择:")

	if user_choice.isdigit():  # 确认输入的是数字（商品编号）
		user_choice = int(user_choice)
		if user_choice < len(product_list): #确定选择的商品在列表中
			p_item = product_list[user_choice]
			if int(p_item[1]) <= salary:  # 确保余额购买的起商品
				shop_car.append(p_item)  # 将商品放入购物车
				salary -= int(p_item[1])  # 扣钱
				print('''
				$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
					  增加商品[%s] 到购物车,您当前余额是 \033[31;1m[%s]\033[0m
				$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
					  '''%(p_item[0], salary))
			else:#余额不足时，提示
				print('''
				$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
				您当前余额是[%s],买不起选中商品%s请充值"
				$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
					  '''% (salary,p_item))
		else: #商品不存在，重新输入
			print('''
					 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
				     ##你选择的商品不存在，重新输入##
				     $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
				     ''')
			continue
	else:	#用户选择q退出或者c查看已购买商品,打印的信息
		if user_choice == 'q':
			print("\033[42m总采购商品如下\033[0m".center(50, '*'))
			for item in shop_car:
				print(item)
			print("结束".center(50, '*'))
			print("您当前余额是%s" % salary)
			exit_flag = True
		elif user_choice == 'c':
			print("\033[41m已采购商品如下\033[0m".center(50, '*'))
			for item in shop_car:
				print(item)
			print("您当前余额是\033[36;1m%s\033[0m" % salary)

#将余额存入文件balance.txt中
str_to_file('balance.txt',salary)

#将购物单存入文件shop_record.txt,并在最后追加时间记录
if len(shop_car) != 0:#只有购物车有商品时才做以下操作
	current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))#调取当前时间
	list_to_file('shop_record.txt', shop_car)#购物车数据写入购物单
	with open('shop_record.txt', 'a', encoding='utf-8') as f:
		f.write(''.join(current_time) + '\n')#写入当前时间至购物单
		f.flush()	#缓存数据刷新










