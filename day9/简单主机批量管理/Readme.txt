#################################################
作者：陈益波
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/
#################################################

作业：批量主机管理工具

程序结构：
.
├── bhms.py
├── conf
│   ├── conf.py # 配置文件
│   └── __init__.py
├── libs
│   ├── __init__.py
│   ├── mylib.py
│   └── progressbar.py
├── logs # 日志目录
│   └── manager.log
├── model # 模型目录
│   ├── __init__.py
│   └── manager.py
└── rsas #秘钥目录
    └── id_rsa

程序配置：配置文件conf.py
import os
BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RSA_DIR = '%s/rsas' %BASE_DIR # 秘钥文件目录

LOG_FILE = '%s/logs/manager.log' %BASE_DIR # 日志文件目录

MULT_NUM = 5 # 进程数

# 分组列表
GROUPS = {
    "group1":['web1'],
    "group2":['web1','web2'],
}
# 主机列表
HOSTS = {
    "web1":{
        "hostname":"192.168.52.129",
        "username":"root",
        "password":"521013",
        "port":22,
        "pkey":os.path.join(BASE_DIR, 'id_rsa'),
    },
    "web2":
    {
        "hostname":"192.168.52.131",
        "username":"root",
        "password":"521013",
        "port":22,
    }
}

# 错误码和错误信息
CODE_LIST = {
    "101" : "Group %s is not exit!",
    "102" : "Host is not exit!",
    "103" : "Options is error, please use -h to see the help doc!",
    "104" : "Commend execute fail",
    "105" : "Module %s is not exit!",
    "106" : "Destination file or dirctory %s is not exit!",
    "107" : "Source file or dirctory %s is not exit!",
}


运行环境：
    1、暂不支持windows主机，Python3.0或以上版本并配置好环境变量（linux主机为了和自带的python2.x版本不冲突，需将python3.X的可执行文件重名为python3或创建名为python3的软链接链接到python的可执行文件）
    2、需要安装第三方的pramiko库，具体安装方法，自己百度

执行方法：
    1、Linux：直接执行# python3 bhms.py 参数或#./bhms.py 参数（需要给主程序文件添加可执行权限）
    2、Windows：暂不支持Windows

使用方法：
    1、参数说明
    Options:
      -h, --help            show this help message and exit # 显示帮助信息
      -g GROUP, --group=GROUP # 主机组名称
                            group name
      -c CMD, --commend=CMD # 远端命令
                            commend
      -m MODULE, --module=MODULE # 模块名 shell（执行远端命令）/file（文件相关操作）
                            module
      -s SRC, --src=SRC     source file or path # 源文件，如果是下载必须使用绝对路径
      -d DST, --dst=DST     destination file or path # 目标目录，如果是上传必须是必须是绝对路径
      -a ACTION, --action=ACTION # 方法，配合file模块，get（下载）/put（上传）
                            action for module file, [get/put]

    2、执行远端命令：bhms.py -m shell -g 组名 -c '命令'
        $ python3 bhms.py -m shell -g group2 -c 'df -h'
        [192.168.52.129] : [df -h]
        Filesystem                   Size  Used Avail Use% Mounted on
        /dev/vda1                     20G   17G  2.4G  88% /
        none                         4.0K     0  4.0K   0% /sys/fs/cgroup
        udev                         7.9G  4.0K  7.9G   1% /dev
        tmpfs                        1.6G  844K  1.6G   1% /run
        none                         5.0M     0  5.0M   0% /run/lock
        none                         7.9G     0  7.9G   0% /run/shm
        none                         100M  4.0K  100M   1% /run/user
        /dev/vdb                     197G  110G   77G  59% /data

        [192.168.52.131] : [df -h]
        Filesystem      Size  Used Avail Use% Mounted on
        /dev/vda1        20G   16G  2.6G  87% /
        none            4.0K     0  4.0K   0% /sys/fs/cgroup
        udev            3.9G  4.0K  3.9G   1% /dev
        tmpfs           799M  860K  798M   1% /run
        none            5.0M     0  5.0M   0% /run/lock
        none            3.9G     0  3.9G   0% /run/shm
        none            100M  4.0K  100M   1% /run/user
        /dev/vdb        197G   49G  139G  27% /data

        注意：如果命令中间有空格，必须用引号引起来