#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen


'''
商家入口
商家修改商品
修改商品对应的价格
'''
import os,sys,codecs

# 将文件转为字典
def getdic(file):
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
def getlist(file) -> object:
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
	with open(file, 'a', encoding='utf-8') as f:
		for key, val in dic.items():
			line = []
			line.append(key)
			line.extend(val)
			f.write(line)
# 将列表写入文件
#追加方式写入信息
def list_to_file1(file, list):
	with open(file, 'a', encoding='utf-8') as f:
			f.write(' '.join(list)+'\n')
			f.flush()
#先清空要打开的文件，继而写入信息
def list_to_file2(file, list):
	with open(file, 'w', encoding='utf-8') as f:
		for line in list:
			f.write(' '.join(line) + '\n')
			f.flush()
		# f.write(' '.join(list) + '\n')

#显示商品信息
def human_display(file,product_list):
	print("\033[41m当前商品信息\033[0m".center(100, "#"))
	product_list = getlist(file)
	for item in enumerate(product_list):
		index = item[0]
		p_name = item[1][0]
		p_price = int(item[1][1])
		print(index, ' ', p_name, p_price)
#显示增加的商品信息
def add_display(file):
	print("\033[42m增加的商品信息\033[0m".center(100,"+"))
	add_list = getlist(file)
	for item in enumerate(add_list):
		index = item[0]
		p_name = item[1][0]
		p_price = int(item[1][1])
		print(' ', p_name, p_price)

product_list = getlist('goods.db')
while True:
	human_display('goods.db',product_list)
	user_choice = input("【\033[31mq退出\033[0m;\033[32mc查看新增加商品列表\033[0m；\033[33ma添加商品\033[0m；\033[34m数字修改商品\033[0m】请选择 :")
	if  user_choice == 'a': #当选择a时添加商品
			add_list = []
			add_product = input("请输入要添加的商品名：")
			add_price = input("请输入要添加的商品的价格：")
			add_list.append(add_product)
			add_list.append(add_price)
			list_to_file1('goods.db',add_list)
			list_to_file1('goods2.db',add_list)#添加至新起的一个文件，便于后面的查看增加的商品信息
	elif user_choice.isdigit():  # 确认输入的是数字（商品编号）
		user_choice = int(user_choice)
		if user_choice < len(product_list):
			# chang_choice = input("请选择是否修改商品[y|n]：")
			print('您选择要修改的商品是[%s]，价格是[%s]' % (product_list[int(user_choice)][0], product_list[int(user_choice)][1]))
			# if chang_choice == 'y':
			new_price = input('请修改价格：')
			product_list[int(user_choice)][1] = new_price
			list_to_file2('goods.db',product_list)
			# elif chang_choice == 'n':
			# 	print("退出修改商品价格")
			# 	break
		else:
			print("您输入的商品不存在，重新输入")
			continue
	elif user_choice == 'q' or user_choice == 'quit':
		human_display('goods.db', product_list)
		break
	elif user_choice == 'c':
		add_display('goods2.db')
	else:
		print('输入有误，请重新输入'.center(100,'-'))
		continue

if os.path.exists('goods2.db'):
	os.remove('goods2.db') #删除增加商品记录的临时文件






