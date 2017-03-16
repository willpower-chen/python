#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/
'''
主程序：实现配置文件的增删改查
'''
from model.haproxy import haproxy
import conf
import collections
import sys

def print_main_menu(items):
    '''
    输出主菜单
    :param items:
    :return: 空
    '''
    menu = enumerate(items, 1)
    print('='*30)
    for menu_item in menu:
        print('%s、%s' %menu_item)
    print('='*30)

def record_to_str(record):
    '''
    将record组装成字符串
    :param record: 一条record记录
    :return: 返回组装好的字符串
    '''
    keys = list(record)
    server = '%s%s %s %s' %(' '*conf.indentation, 'server', record[keys[0]], record[keys[0]])
    for k in keys[1:]:
        server = '%s %s %s' %(server, k, record[k])
    return server

def find_backend_record():
    flag = True
    while flag:
        backend_name = input("请输入backend（r返回上级菜单，q退出）：").strip() # 获取用户输入的backendname
        if backend_name == 'r': #判断用户是否输入的r
            flag = False # 退出循环返回到主菜单
        elif backend_name == 'q':
            sys.exit('已退出程序')
        else:
            records = haproxy.get_backend(backend_name) # 调用haproxy的get_backend方法返回的backend信息
            if records:# 判断返回的是否为空
                # 不为空说明存在，执行
                for record in records: #遍历backend的record
                    server = record_to_str(record) # 调用record_to_str方法将record组装成字符串
                    print(server) # 显示record信息
            else:
                print('没有找到，请检查输入是否正确')
            input('输入任意键继续')


def get_backend_str():
    '''
    把所有backend转化为符合配置文件格式的字符串，用于输出显示和写入到文件
    :return: # 返回经过格式化的字符串
    '''
    backends = haproxy.get_backends()
    backend_str = ''
    for backend in backends: # 遍历所有baekend
        backend_str = ''.join([backend_str, '%s %s\n' %('backend',backend['backend'])]) # 格式化backend
        for record in backend['record']: # 遍历backend下面的记录
            server = record_to_str(record) # record_to_str函数返回record的字符串
            backend_str = ''.join([backend_str, server, '\n'])
    return backend_str

def show_backends():
    '''
    显示当前所有backend信息
    :return: 无
    '''
    backend_str = get_backend_str() #调用get_backend_str方法获取格式化好的所有backend信息
    print(backend_str)


def insert_backend_record():
    '''
    插入或修改record信息
    :return: 无
    '''
    flag = True
    while flag:
        record = input("\033[31;1m请输入要新加的记录（r返回上级菜单）\033[0m：").strip() #获取用户输入的字符串
        if record == 'r': # 如果是r退出循环，返回上级菜单
            flag = False
        elif record == 'q':
            sys.exit('已退出程序')
        else:
            import json
            try:
                tmp_dic = json.loads(record) # 将用户输入的json格式字符串转为python字典格式
            except Exception:
                # 如果转化异常说明如数的格式有错误
                input('输入的格式错误，按任意键继续')
                continue
            record = tmp_dic.get('record') # 获取record
            backend_name = tmp_dic.get('backend') # 获取backend名称
            if record and backend_name: #判断record和backend是否为空，如果有一个为空说明输入的不合法
                #print(record)
                record_ord_dic = collections.OrderedDict() # 定义空的有序字典保存record信息
                #print(record.keys())
                if haproxy.check_record_option_key(record.keys()) and haproxy.check_record_option_type(record): # 判断record的options是否合法
                    # 合法执行
                    if haproxy.check_ip(tmp_dic.get('record').get('server')): # 检查server字段是否存在且ip地址是否合法
                        for op in conf.record_op_list: # 通过遍历conf.py的record_op_list的顺序获取record的对应的值
                            record_value = record.get(op) # 从用户输入的获取对应的值
                            if record_value: # 如果这个值存在，加入到用来保存record信息的有序字典中
                                record_ord_dic[op] = record_value
                        #print(record_ord_dic)
                        haproxy.add_record(backend_name,record_ord_dic) # 调用haproxy的add_record方法加入到指定backend节点中
                        input('添加或修改成功，按任意键继续')
                    else:
                        input('输入ip地址不合法请检查，或不存在server字段，按任意键继续')
                        pass
                else:
                    input('输入record包含不合法关键字或record参数类型错误，请检查，按任意键继续')
                    pass
            else:
                input('输入错误，请检查json字符串的第一层key是否包含是否包含backend或record，按任意键继续')
                pass
def del_record():
    '''
    删除记录函数
    :return:
    '''
    flag = True

    while flag:
        record = input("\033[31;1m请输入要删除的记录（r返回上级菜单）\033[0m：").strip() #获取用户输入的字符串
        if record == 'r': # 如果是r退出循环，返回上级菜单
            flag = False
        elif record == 'q':
            sys.exit('已退出程序')
        else:
            import json
            try:
                tmp_dic = json.loads(record) # 将用户输入的json格式字符串转为python字典格式
            except Exception:
                input('输入的格式错误，按任意键继续')
                continue
            record = tmp_dic.get('record') # 获取record
            backend_name = tmp_dic.get('backend') # 获取backend名称
            if backend_name and record: # 判断是否存在backend和record字段
                server_name = tmp_dic.get('record').get('server') # 获取ip地址
                if haproxy.check_ip(server_name): # 检测ip地址是否合法
                    if haproxy.del_record(backend_name, server_name): # 调用haproxy的del_record方法删除record
                        input('删除成功，按任意键继续')
                        pass
                else:
                    input('输入ip地址不合法请检查，或不存在server字段，按任意键继续')
                    pass
            else:
                input('输入错误，请检查json字符串的第一层key是否包含是否包含backend或record，按任意键继续')
                pass
    pass

def write_to_file():
    '''
    将临时保存的haproxy配置文件信息保存到haproxy配置文件中
    :return:
    '''
    choose = input('确认保存修改y|n返回上层）（q退出程序）: ') # 获取用户确认
    if choose == 'y':
        backends = haproxy.get_backends() # 获取所有backend
        backend_str = get_backend_str() # 将所有backend信息转化为字符串形式
        if haproxy.write_to_file(backend_str): # 调用haproxy的write_to_file方法，写入到文件，判断是否成功写入到文件
            input('写入文件成功，按任意键继续')
        else:
            input('写入文件失败，按任意键继续')
    elif choose == 'q':
        sys.exit('已退出程序')
    elif choose == 'n':
        print('返回上层目录')
        pass

if __name__ == '__main__':
    haproxy = haproxy(conf.haproxy_file)
    flag = True
    while flag:
        print_main_menu(conf.main_menu)
        choose = input('\033[31;1m请输入操作编号（输入q退出系统）\033[0m：').strip()
        if choose == '1':                   #选择1查询
            find_backend_record()
        elif choose == '2':                 #选择2增加修改
            insert_backend_record()
        elif choose == '3':                 #选择3删除
            del_record()
        elif choose == '4':                 #选择4确认修改，保存备份文件
            write_to_file()
        elif choose == '5':                 #选择5查询所有backend记录
            show_backends()
            input('按任意键继续')
        elif choose == 'q':                 #选择q退出
            flag = False
        else:                               #空或输入错误，提示重新输入
            input('输入错误，按任意键继续')