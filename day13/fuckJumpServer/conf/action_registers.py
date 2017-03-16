#_*_coding:utf-8_*_
__author__ = 'Alex Li'

from modules import views

actions = {
    'start_session': views.start_session, #开启会话，
    # 'stop': views.stop_server,
    'syncdb': views.syncdb,#创建库
    'create_users': views.create_users,#创建堡垒机用户表
    'create_groups': views.create_groups, #创建用户组表
    'create_hosts': views.create_hosts,#创建主机表
    'create_bindhosts': views.create_bindhosts,#创建bindhost表
    'create_remoteusers': views.create_remoteusers,#创建远程用户表
    'audit':views.log_audit#创建日志表

}