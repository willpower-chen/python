#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/
'''
运算模块
'''

import re


class calculator(object):
	def __init__(self):
		'''
        构造方法，用来初始化所有用到的正则表达式
        '''
		# 匹配有一个括号的，用来提取括号内的字串
		self.__one_parentheses_ex = '\([^\(\)]+\)'
		# 检查不加括号的表达式是否合法
		self.__check_no_parentheses_ex = '^[\+\-]{0,1}\d+[\.]{0,1}\d*([\+\-\*\/]{1}[\+\-]{0,1}\d+[\.]{0,1}\d*)+$'
		# 匹配乘除法表达式
		self.__multiplication_division_ex = '[\+\-]{0,1}\d+[\.]{0,1}\d*[\*\/]{1}[\+\-]*\d+[\.]{0,1}\d*'
		# 匹配加减法表达式
		#self.__add_sub_ex = '[\+\-]{0,1}\d+[\.]{0,1}*\d*[\+\-]+\d+[\.]*\d*'
		self.__add_sub_ex = '[\+\-]{0,1}\d+[\.]*\d*[\+\-]+\d+[\.]*\d*'
		# 匹配单个数字，用于括号内只有一个数字的情况，例如（-1.0）
		self.__is_num = '^[\+\-]{0,1}\d+[\.]{0,1}\d*$'
		# 匹配多个连续正号、负号的情况，用于替换多个符号
		self.__mult_sign = '[\+\-]{2,}'

	def __replace_sign(self,expression):
			'''
			替换多个连续+-符号的问题
			:param self:
			:param expression: 表达式，包括有括号的情况
			:return: 返回经过处理的表达式
			'''
			def re_sign(m):
				if m:
					if m.group().count('-')%2 == 1:
						return '-'
					else:
						return '+'
				else:
					return ''
			expression = re.sub(self.__mult_sign,re_sign,expression)
			return expression

	def __multiplication_division(self, expression):
			'''
			逐一找出乘除法表达式，并计算出所有表达式的结果
			:param self:
			:param expression: 四则运算表达式
			:return: 返回去除了乘除法的四则运算表达式，只剩下加减法
			'''
			expression = self.__replace_sign(expression)
			#查找最基本的乘除法表达式，只包含两个数和运算符号
			res = re.search(self.__multiplication_division_ex,expression)
			if res:#包含乘除法
				res = res.group()
				#获得表达式的两个数
				num1,num2 = re.findall('[\+\-]{0,1}\d+[\.]{0,1}\d*',res)
				operate = re.search('[\*\/]',res).group()#获取符号
				result = self.__base_arithmetic(num1,operate,num2)#计算
				expression = expression.replace(res,result)#将结果替换到表达式中
				#进行递归，继续查找并计算基本乘除法表达式
				return self.__multiplication_division(expression)
			else:
				#如果不包含最基本表达式，说明乘除法计算完毕，返回表达式，结束递归
				return expression

	# def __add_subtraction(self, expression):
	# 	'''
     #    将只包含加减法的表达式进行计算，并返回结果
     #    :param expression: 加减法运算表达式
     #    :return: 返回计算结果
     #    '''

	def __add_subtraction(self, expression):
			'''
			将只包含加减法的表达式进行计算，并返回结果
			:param self:
			:param expression:
			:return:
			'''
			expression = self.__replace_sign(expression)
			res = re.search(self.__add_sub_ex, expression)
			if res:
				res = res.group()
				num1, num2 = re.findall('[\+\-]{0,1}\d+[\.]{0,1}\d*', res)
				operate = '+'#这里为什么符号是加号，因为减法例如2-1相当于2+（-1）
				#result = self.__base_arithemtic(num1, operate, num2)#加减法运算
				result = self.__base_arithmetic(num1, operate, num2)#加减法运算
				expression = expression.replace(res,result)
				return self.__add_subtraction(expression)#递归处理加减法表达式
			else:
				#找不到加减法表达式，就返回结果
				return expression

	def __four_arithmetic_operation(self, expression):
			'''
			进行没有括号的四则运算
			:param self:
			:param expression: 四则运算表达式
			:return: 运算结果
			'''
			expression = self.__replace_sign(expression)#去除连续加减号
			#expression = self.__multiplication_division(expression)#先计算乘除法
			expression = self.__multiplication_division(expression)
			expression = self.__add_subtraction(expression)#计算加减法
			return expression

	def __base_arithmetic(self, num1, operate, num2):
			'''
			基础运算方法，计算两个数的加减乘除结果
			:param self:
			:param num1: 第一个数
			:param operate: 计算符号
			:param num2: 第二个数
			:return: 计算结果
			'''
			try:
				num1 = float(num1)
				num2 = float(num2)
			except Exception:
				return None
			if operate == "+":
				result = num1 + num2
			elif operate == "-":
				result = num1 - num2
			elif operate == "*":
				result = num1 * num2
			elif operate == "/":
				result = num1 / num2
			else:
				return None
			if result >= 0:
				'''如果最后的值大于0返回的值前面加"+"正好,
				避免1-2*-3中-2*-3被乘法表达为-2*-3=6,
				得出最后的结果为16
				'''
				return '%s%s'%('+',result)
			else:
				return str(result)

	def __parentheses(self, expression):
			'''
			逐一将括号内的表达式取出来，
			如果取出来的四则运算表达式合法，进行四则运算
			如果不合法返回Flase
			:param self:
			:param expression:带括号的四则运算表达式
			:return: 不带括号的四则运算表达式或者Flase
			'''
			#搜索只有一个括号的表达式
			res = re.search(self.__one_parentheses_ex,expression)
			while res:
				res = res.group()
				#把表达式的左右括号去掉（替换为空），
				res_tmp = res.replace('(',"").replace(')',"")
				if re.match(self.__is_num,res_tmp):#判断括号内是否只是数字
					result = res_tmp #是，直接返回结果
				else:#不是只有数字，进行四则运算
					if not self.__check_expression(res_tmp): #四则运算不合法，返回False
						return False
					else:#合法，进行四则运算
						result = self.__four_arithmetic_operation(res_tmp)
				expression = expression.replace(res,result)
				res = re.search(self.__one_parentheses_ex,expression)
			return expression

	def __check_expression(self, expression):
			'''
			判断不带括号的四则运算表达式是否合法
			:param self:
			:param expression: 不带括号的表达式
			:return: 合法True，不合法False
			'''
			if re.match(self.__check_no_parentheses_ex,expression):
				return True
			else:
				return False

	def getResult(self, expression):
			'''
			计算带括号的四则运算的值，用来外部调用
			:param self:
			:param expression: 带括号的四则运算表达式
			:return: 最终结果
			'''
			expression = self.__replace_sign(expression)
			expression = self.__parentheses(expression)
			if not expression:
				return False
			else:
				expression = self.__replace_sign(expression)
				if self.__check_expression(expression):#判断表达式合法性
					return self.__four_arithmetic_operation(expression)
				else:
					return False
