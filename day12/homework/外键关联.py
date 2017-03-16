#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DATE,Column,Integer,String,ForeignKey,UniqueConstraint,Index
from sqlalchemy.orm import sessionmaker,relationship

engine = create_engine("mysql+pymysql://root:521013@192.168.52.113/cgpower",
					   encoding= "utf-8" )
Base = declarative_base()
class Student(Base):
	__tablename__ = 'student'
	id = Column(Integer,primary_key=True)
	name = Column(String(32),nullable=False)
	register_date = Column(DATE,nullable=False)
	def __repr__(self):
		return "<User(name='%s',  password='%s')>" % (
			self.name, self.password)

class Stuy_record(Base):
	__tablename__ = 'study_record'
	id = Column(Integer,primary_key=True)
	day = Column(Integer,nullable=False)
	status = Column(Integer,nullable=False)
	stu_id = Column(Integer, ForeignKey("student.id"))
	student = relationship("Student_test", backref="my_study_record")
	def __repr__(self):
		return "<%s day:%s status:%s>" % (self.student_test.name,self.day,self.status)


s1 = Student(name="Alex",register_date = "2014-05-21")
s2 = Student(name="Jack",register_date = "2013-04-21")
s3 = Student(name="hameimei",register_date = "2012-03-21")
s4 = Student(name="lilei",register_date = "2011-02-21")

study_obj1 = Stuy_record(day=1,status="YES", stu_id=1)
study_obj2 = Stuy_record(day=2,status="NO", stu_id=1)
study_obj3 = Stuy_record(day=3,status="YES", stu_id=1)
study_obj4 = Stuy_record(day=1,status="YES", stu_id=2)
#
Base.metadata.create_all(engine)
Session_class = sessionmaker(bind=engine)
session = Session_class()
session.add_all([s1,s2,s3,s4,study_obj1,study_obj2,study_obj3,study_obj4])

# stu_obj = session.query(Student).filter(Student.name=="alex").first()
# print(stu_obj.my_study_record)
session.commit()