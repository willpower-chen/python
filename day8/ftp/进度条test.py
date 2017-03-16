#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/

import sys,time

output = sys.stdout
for count in range(0,100):
    second = 1
    time.sleep(second)
    output.write('#')
    output.flush()
