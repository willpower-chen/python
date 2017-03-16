#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/
IP_PORT = ('127.0.0.1',9999)

USERS_FILE = 'dbs/users.db'

FILE_PER_SIZE = 1024

TMP_SPACE_SIZE = 1024 * 1024 * 1024

CODE_LIST = {
    '200': "Pass authentication!",
    '201': "Authentication fail wrong username or password",
    '300': "Ready to send file to client",
    '301': "Client ready to receive file data ",
    '302': "File doesn't exist",
    '303': "Path doesn't exist",
    '304': "Destination path doesn't exist",
    '305': "IO error",
    '306': "Socket error",
    '307': "Insufficient space",
    "308": "Validate successful",
    "309": "Validate fail",
    "310": "Path or file doesn't exixt",
    '401': "Invalid instruction!",
    '500': "Invalid execute successful",
    '501': "Invalid execute fail",
}

JINDO_MAX = 40


