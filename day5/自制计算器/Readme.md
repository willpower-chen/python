﻿
# @author: 陈益波
# Email: 492475981@qq.com
# Blog: http://www.cnblogs.com/willpower-chen/


作业：
    实现加减乘除及拓号优先级解析
    用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )等类似公式后，
    必须自己解析里面的(),+,-,*,/符号和公式(不能调用eval等类似功能偷懒实现)，运算后得出结果，结果必须与真实的计算器所得出的结果一致




具体操作流程：
请输入四则运算表达式，输入"q"退出程序
例如：1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
>>> 1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
myEval: 2776672.6952380957
按任意键继续
请输入四则运算表达式，输入"q"退出程序
例如：1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
>>> - -(1.1+1+1 -( -1) -(1+1 + (1+1+2.2))) + - - - - -111 + - - + + - - 3 - + + + + +889
myEval: -999.1
按任意键继续
请输入四则运算表达式，输入"q"退出程序
例如：1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
>>> - -(1.1+1+1 -( -1) -(1+1 + (1+1+2.2))) + - - - dddd- -111 + - - + + - - 3 - + + + + +889
输入的表达式不正确，请检查
请输入四则运算表达式，输入"q"退出程序
例如：1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
>>> q

