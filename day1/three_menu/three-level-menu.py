#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
'''
三级菜单
'''

#一级菜单
def menu():
	#遍历字典dic一级菜单
	print('----------一级菜单------------')
	for index,key in enumerate(dic.keys(),1):
		print(index,key)
		##将一级key的下标与key放入临时字典中
		dic_key[str(index)]=key
	choose = input('请选择1级菜单！退出输入q，返回输入b: ')
	#判断输入，输入q时退出，输入b时提示无法返回
	if choose == 'q':
		quit()
	elif choose == 'b':
		print('目前为一级目录，无法返回，请重新选择！')
		menu()
	#判断用户输入是否在临时字典的key中，若有调用二级菜单
	elif dic_key.get(choose,0):
		menu_1(dic_key[choose])
	else:
		print('')
		print('您的输入有误，请重新输入！')

#二级菜单
def menu_1(choose1):
	#输入有误时重新加载二级菜单项
	while True:
		print('')
		print('------二级菜单------')
		#遍历字典dic二级菜单
		for index,key in enumerate(dic[choose1].keys(),1):
			print(index,key)
			#将二级key的下标与key放入临时字典中
			dic_key[str(index)] = key
		choose2 = input("请选择2级菜单！退出输入q，返回请输入b：")
		#判断输入，输入q时退出，输入b时，调用1级菜单
		if choose2 =='q':
			quit()
		elif choose2 =='b':
			menu()
		elif dic_key.get(choose2,0):
			menu_2(choose1,dic_key[choose2])
		else:
			print('')
			print('您输入有误，请重新输入')
#三级菜单项
def menu_2(choose1,choose2):
	#输入有误时重新加载三级菜单项
	while True:
		#遍历字典dic三级菜单
		print('')
		print('------三级菜单------')
		for index,key in enumerate(dic[choose1][choose2],1):
			#显示key与key的下标
			print(index,key)
			#将三级key的下标与key放入临时字典中
			dic_key[str(index)] =key
		choose3 = input("请选择3级菜单！退出输入q，返回第二层请输入b，直接返回第一层请输入c：")
		#判断输入，输入q时退出，输入b时调用上级菜单,输入c时返回第一级菜单
		if choose3 == 'q':
			quit()
		elif choose3 == 'b':
			menu_1(choose1)
		elif choose3 == 'c':
			menu()
		else:
			print('')
			print("已经是最后一层！")


if __name__ == '__main__':
	#设置菜单
	dic = {
		"福建省": {
			"龙岩市": ["新罗区", "永定区", "上杭区"],
			"厦门市": ["湖里区", "集美区", "海沧区"]
		},
		"浙江省": {
			"苏州市": ["吴中区", "相城区"],
			"杭州市": ["西湖区", "上城区"]
		}
	}
	dic_key = {}
	while True:
		menu()


