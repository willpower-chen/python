#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/
from sqlalchemy import Table, Column, Integer,String,DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base() # 生成所有sqlorm的基类

ClassroomToStudent = Table('classroom_to_student', Base.metadata,
                        Column('classroom_id',Integer,ForeignKey('classroom.id')),
                        Column('student_id',Integer,ForeignKey('student.id')),
                        )

class Student(Base):
	__tablename__ = 'student'
	id = Column(Integer,primary_key=True)
	name = Column(String(32),nullable=False)
	results = Column(Integer,nullable=False)
	register_date = Column(DATE,nullable=False)
	def __repr__(self):
		return "<User(name='%s',  password='%s')>" % (
			self.name, self.password)

class Classroom(Base):
	__tablename__ = 'classroom'
	id = Column(Integer,primary_key=True)
	name = Column(String(32),nullable=False)
	cursers = Column(Integer,nullable=False)
	stu_id = Column(Integer, ForeignKey("student.id"))
	students = relationship('Student', secondary=ClassroomToStudent, backref='classrooms')
	def __repr__(self):
		return "<%s cursers:%s >" % (self.name,self.cursers)





