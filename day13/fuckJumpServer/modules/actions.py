__author__ = "Alex Li"

from conf import action_registers
from modules import utils

def help_msg():#
    '''
    print help msgs
    :return:
    '''
    print("\033[31;1mAvailable commands:\033[0m") #打印帮助信息
    for key in action_registers.actions:#action_registers里的命令循环打印
        print("\t",key)

def excute_from_command_line(argvs):
    if len(argvs) < 2: #没有输入命令及参数，打印帮助信息，并退出
        help_msg()
        exit()
    if argvs[1] not in action_registers.actions: #输入的命令不存在的话，就退出。
        utils.print_err("Command [%s] does not exist!" % argvs[1], quit=True)
    action_registers.actions[argvs[1]](argvs[1:])#获取命令及参数