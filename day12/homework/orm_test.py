#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:521013@192.168.52.113/cgpower_test",
					   encoding= "utf-8" )
Base = declarative_base()
class User(Base):
	__tablename__ = 'user'
	id = Column(Integer,primary_key=True)
	name = Column(String(32))
	password = Column(String(64))
	def __repr__(self):
		return "<User(name='%s',  password='%s')>" % (
			self.name, self.password)
Base.metadata.create_all(engine)
Session_class = sessionmaker(bind=engine)
Session = Session_class()
user_obj = User(name = 'cjk',password = '123456')
user_obj2 = User(name = 'lzll',password = '123456')
# print(user_obj.name,user_obj.id)
# Session.add(user_obj)
# Session.add(user_obj2)
# print(user_obj.name,user_obj.id)
my_user = Session.query(User).filter_by().all()
print(my_user)

Session.commit()
