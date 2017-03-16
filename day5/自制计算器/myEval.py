#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/
'''
用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
等类似公式后，必须自己解析里面的(),+,-,*,/符号和公式，运算后得出结果，结果必须与真实的计算器所得出的结果一致
'''
from calculator_module.calculator import calculator

if __name__ == '__main__':
	calculator = calculator()
	while True:
		print('请输入四则运算表达式，输入"q"退出程序')
		print('例如：1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))')
		#去除两边和中间的空格
		expression = input('>>> ').strip().replace(' ','')
		if expression == 'q':
			break
		else:
			#调用calulator对象的getResult函数进行运算，得到结果
			result = calculator.getResult(expression)
			if result: # 判断结果是否为正确的结果（如果返回的数值说明表达式正确，如果返回的事False说明表达式不合法）
				print('myEval:',float(result))
			else:
				print('输入的表达式不正确，请检查')
				continue
		# else:
		# 	break
		input('按任意键继续')