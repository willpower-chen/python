from django.shortcuts import render,redirect,HttpResponse
# Create your views here.
from cmdb import models
import json

#获取业务线数据的三种方式
def business(request):
	#对象
	v1 = models.Business.objects.all()
	#字典
	v2 = models.Business.objects.all().values()
	#元组
	v3 = models.Business.objects.all().values_list()
	return render(request,'business.html',{'v1':v1,'v2':v2,'v3':v3,})

def host(request):
	if request.method == 'GET':
		#对象
		v1 = models.Host.objects.all()
		#字典
		v2 = models.Host.objects.all().values('id','hostname','ip','port','b_id','b__caption')
		#元组
		v3 = models.Host.objects.all().values_list('id','hostname','ip','port','b_id','b__caption')
		b_list = models.Business.objects.all()
		return render(request,'host.html',{'v1':v1,'v2':v2,'v3':v3,'b_list':b_list})
	elif request.method=='POST':
		h = request.POST.get('hostname')
		i = request.POST.get('ip')
		p = request.POST.get('port')
		b = request.POST.get('b_id')
		models.Host.objects.create(hostname=h,
								   ip=i,
								   port=p,
								   b_id=b,)

		return redirect('/host/')

#数据删除
def test_delete(request):
	hid = request.POST.get('hid')
	print(hid)
	models.Host.objects.filter(id=hid,).delete()
	return HttpResponse('数据已经删除')

#数据编辑
def ajax_submit_edit(request):
	ret = {'status': True, 'error': None, 'data': None,}
	try:
		hid = request.POST.get('id')
		h = request.POST.get('hostname')
		i = request.POST.get('ip')
		p = request.POST.get('port')
		b = request.POST.get('b_id')
		if h and len(h) > 5:
			models.Host.objects.filter(id=hid).update(hostname=h,
									   ip=i,
									   port=p,
									   b_id=b, )
		else:
			ret['status'] = False
			ret['error'] = '太短了'
	except Exception as e:
		ret['status'] = False
		ret['error'] = str(e)
	return HttpResponse(json.dumps(ret))

def test_ajax(request):
	ret = {'status': True, 'error': None, 'data': None,}
	try:
		h = request.POST.get('hostname')
		i = request.POST.get('ip')
		p = request.POST.get('port')
		b = request.POST.get('b_id')
		if h and len(h) > 5:
			models.Host.objects.create(hostname=h,
									   ip=i,
									   port=p,
									   b_id=b, )
		else:
			ret['status'] = False
			ret['error'] = '太短了'
	except Exception as e:
		ret['status'] = False
		ret['error'] = str(e)
	return HttpResponse(json.dumps(ret))

#通过form表单的应用添加
def app(request):
	if request.method ==  "GET":
		app_list = models.Application.objects.all()
		host_list = models.Host.objects.all()

		return render(request,'app.html',{'app_list':app_list,'host_list':host_list,})
	elif request.method == 'POST':
		app_name = request.POST.get('app_name')
		#注意这里是获取一个列表，用getlist
		host_list = request.POST.getlist('host_list')
		obj = models.Application.objects.create(name=app_name)
		obj.r.add(*host_list)
		return redirect('/app')

#通过ajax来对app的添加
def app_ajax_add(request):
	ret = {'status':True,'error':None,'data':None,}
	try:
		app_name = request.POST.get('app_name')
		host_list = request.POST.getlist('host_list')

		if app_name:
			obj = models.Application.objects.create(name=app_name)
			obj.r.add(*host_list)

		else:
			ret['status'] = False
			ret['error'] = '应用名不能为空'
	except Exception as e:
		ret['status'] = False
		ret['error'] = str(e)

	return HttpResponse(json.dumps(ret))








#增加主机和业务

def add_host_business(request):
	b_l = [
		{'caption':'运维部',},
		{'caption':'测试',},
		{'caption':'开发',},
		{'caption':'市场',},
	]
	for i in b_l:
		models.Business.objects.create(**i)


	h_l = [
	{'hostname':'wuhan.cgpower.cn','ip':'192.168.1.110','port':'8001','b_id': 1,},
	{'hostname':'nanjing.cgpower.cn','ip':'192.168.1.111','port':'8002','b_id': 2,},
	{'hostname':'qindao.cgpower.cn','ip':'192.168.1.112','port':'8003','b_id': 1,},
	{'hostname':'chongqing.cgpower.cn','ip':'192.168.1.113','port':'8004','b_id': 2,},
	]
	for row in h_l:
		obj = models.Host(**row)
		obj.save()
	return HttpResponse('add OK')
