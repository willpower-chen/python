from django.db import models

# Create your models here.
class Userlist(models.Model):
	username = models.CharField(max_length=32)
	password = models.CharField(max_length=32,default='123456')
	email = models.CharField(max_length=32)
	c = models.ForeignKey(to='City',to_field='id')

class City(models.Model):
	cityname = models.CharField(max_length=32)

class Business(models.Model):
	caption = models.CharField(max_length=32)
	code = models.CharField(max_length=32,null=True,default='SA')

class Host(models.Model):
	hostname = models.CharField(max_length=32,db_index=True)
	ip = models.GenericIPAddressField(db_index=True)
	port = models.IntegerField()
	b = models.ForeignKey(to='Business',to_field='id')

class Application(models.Model):
	name = models.CharField(max_length=32,db_index=True)
	#自动创建多对多关系表
	r = models.ManyToManyField('Host')

#自定义创建多对多关系表
# class HostToApplication(models.Model):
# 	hobj = models.ForeignKey('Host')
# 	aobj = models.ForeignKey('Application')

