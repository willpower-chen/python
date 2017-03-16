#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from conf import conf

engine = create_engine(conf.DB)
SessionCls = sessionmaker(bind = engine)
session = SessionCls()