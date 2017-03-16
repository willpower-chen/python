from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from app01 import models
from django.views import View
# Create your views here.
USER_DICT = {
	'k1':"root1",
	'k2':"root2",
	'k3':"root3",
	'k4':"root4",
}

def login(request):
	return render(request,'login.html')

def index(request):
	return  render(request,'index.html',{'user_dict': USER_DICT})

class Home(View):
	def dispatch(self, request, *args, **kwargs):
		print('before')
		result = super(Home,self).dispatch(request, *args, **kwargs)
		print('after')
		return result

	def get(self,request):
		print(request.method)
		return render(request,'home.html')
	def post(self,request):
		print(request.method)
		return render(request,'home.html')

def detail1(request, *args):
	print(args)
	return HttpResponse(args)

def detail2(request,**kwargs):
	print(kwargs['uid'],kwargs['nid'])
	return HttpResponse(kwargs['uid','nid'])


def orm(request):
	#增
	# models.UserInfo.objects.create(username='root',password='123')

	# dic = {'username':'eric','password':'456'}
	# models.UserInfo.objects.create(**dic) #注意**

	# obj = models.UserInfo(username = 'lzll',password = '666')
	# obj.save()

	#查
	# result = models.UserInfo.objects.all()
	# for row in result:
	# 	print(row.id,row.username,row.password)

	# result =models.UserInfo.objects.filter(username='root',password='123')
	# for row in result:
	# 	print(row.id, row.username, row.password)

	#删除
	# models.UserInfo.objects.filter(username='lzll').delete()

	#更新
	models.UserInfo.objects.filter(username='root').update(password='69')

	return HttpResponse('orm')

