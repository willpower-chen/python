#作者信息
***author:陈益波
***nickname: willpower-chen
***myblog: http://www.cnblogs.com/willpower-chen/
***mygithup: https://github.com/willpower-chen


功能：实现配置文件的增删改查

主入口haproxy_configuration.py

修改Haproxy配置文件
    1、获取ha记录通过用户输入的backend名称显示该backend下所有记录
    2、新增或修改ha记录，用户输入类似：{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}，分为如下3种情况
       1）如果backend存在查看是否有ip地址相同的记录，如果没有则添加没。
       2）如果有ip地址相同的记录，则修改ha记录。
       3）如果backend不存在则新建backend，并添加记录
    3、删除，用户输入类似{"backend": "test.oldboy.org","record":{"server": "100.1.7.9"}}删除对应的记录，如果一个backend的记录已经为空了，删除backend
    4、将修改写入到文件：通过用户输入确认，将当前所有修改保存到文件
    5、显示全部backend：显示所有backend的所有record