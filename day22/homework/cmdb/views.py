from django.shortcuts import render,redirect,HttpResponse
# Create your views here.
from utils import pagination
from cmdb import models
import json,datetime
from django.views.decorators.cache import cache_page

from django import forms
from django.forms import widgets
from django.forms import fields
from cmdb import models

class FM(forms.Form):
    # 字段本身只做验证
    user = fields.CharField(
        error_messages={'required': '用户名不能为空.'},
        # widget=widgets.Textarea(attrs={'class': 'c1'}),
        label="用户名",
        )
    pwd = fields.CharField(
        max_length=12,
        min_length=6,
        error_messages={'required': '密码不能为空.', 'min_length': '密码长度不能小于6', "max_length": '密码长度不能大于12'},
        widget=widgets.PasswordInput(attrs={'class': 'c2'}),
		label="密码",
    )
    email = fields.EmailField(label="email",error_messages={'required': '邮箱不能为空.','invalid':"邮箱格式错误"})

    f = fields.FileField()
    # p = fields.FilePathField(path='app01')
	# 单选框
    city1 = fields.ChoiceField(
        choices=[(0,'上海'),(1,'广州'),(2,'东莞')]
    )
	# 复选框
    city2 = fields.MultipleChoiceField(
        choices=[(0,'上海'),(1,'广州'),(2,'东莞')]
    )

def fm(request):
    if request.method == "GET":
        # 从数据库中吧数据获取到
        dic = {
            "user": 'root',
            'pwd': '123123',
            'email': 'root@qq.com',
            'city1': 1,
            'city2': [1,2]
        }
        obj = FM(initial=dic)
        return render(request,'fm.html',{'obj': obj})
    elif request.method == "POST":
        # 获取用户所有数据
        # 每条数据请求的验证
        # 成功：获取所有的正确的信息
        # 失败：显示错误信息
        obj = FM(request.POST)
        r1 = obj.is_valid()
        if r1:
            # obj.cleaned_data
            models.Userlist.objects.create(**obj.cleaned_data)
        else:
            # ErrorDict
            # print(obj.errors.as_json())
            # print(obj.errors['user'][0])
            return render(request,'fm.html', {'obj': obj})
        return render(request,'fm.html')



# 缓存
@cache_page(10)
def cache(request):
    import time
    ctime = time.time()
    return render(request, 'cache.html', {'ctime': ctime})

# session的验证
def login(request):
	if request.method == 'GET':
		return render(request,'login.html')
	if request.method == 'POST':
		u = request.POST.get('username')
		p = request.POST.get('pwd')
		t = models.Userlist.objects.filter(username=u)
		##当用户不存在时，返回login登陆界面
		if not t:
			return render(request,'login.html')
		else:
			obj = models.Userlist.objects.get(username=u)
		#当密码正确时，进入跳转到'/host/'这个url，并且增加一个cookie
		if obj.password==p:
			request.session['username'] = u
			request.session['is_login'] = True
			if request.POST.get('rmb', None) == '1':
				# 设置免登陆超时时间5秒
				request.session.set_expiry(5)
				return redirect('/host/')
			# 不设置免登陆时间默认是两周
			return redirect('/host/')
		else:
			return render(request, 'login.html')


		#cookie代码配置
		# 	res = redirect('/host/')
		# 	#set_cookie的参数有key键，value值，max_age超时失效单位秒,
		# 	# res.set_cookie('username1',u,max_age=5)
		# 	#获取当前时间current_date
		# 	current_date = datetime.datetime.utcnow()
		# 	#设置相对当前时间，500秒后失效（截止时间失效）
		# 	delay_time = current_date + datetime.timedelta(seconds=500)
		# 	res.set_cookie('username1',u,expires=delay_time)
		# 	return res
		# else:
		# 	return render(request,'login.html')

#注销
def logout(request):
	# 清除用户对应的session数据
	request.session.clear()
	return redirect('/login/')

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


	# #首先获取cookie上的值
	# v = request.COOKIES.get('username1')
	# #如果cookie不存在，直接跳转到login登陆页面，如果cookie存在，即跳转到host页面
	# if not v:
	# 	return redirect('/login/')

	#session中获取数据
	#直接用request.session['is_login']时，当去不到值时，host刷新会报错，所以要用request.session.get('is_login')
	# 如果is_login不存在则返回登陆页面
	if not request.session.get('is_login'):
		return redirect('/login/')
	# 如果is_login存在继续
	elif request.session.get('is_login'):
		if request.method == 'GET':
			#对象
			v1 = models.Host.objects.all()
			b_list = models.Business.objects.all()
			#分页
			t = models.Host.objects.all().count()
			LIST = []
			for i in range(1,int(t)+1):
				LIST.append(i)
			current_page = request.GET.get('p', 1)
			current_page = int(current_page)
			val = request.COOKIES.get('per_page_count')
			if not val:
				page_obj = pagination.Page(current_page, len(LIST))
			else:
				val = int(val)
				page_obj = pagination.Page(current_page, len(LIST), val)

			data = v1[page_obj.start:page_obj.end]
			page_str = page_obj.page_str('/host/')
			# return render(request,'host.html',{'current_user': v,'page_str':page_str,'data':data,'b_list':b_list})
			return render(request,'host.html',{'page_str':page_str,'data':data,'b_list':b_list})

		elif request.method=='POST':
			h = request.POST.get('hostname')
			i = request.POST.get('ip')
			p = request.POST.get('port')
			b = request.POST.get('b_id')
			models.Host.objects.create(hostname=h,
									   ip=i,
									   port=p,
									   b_id=b,)
			# return render(request, 'host.html', {'current_user': v})
			return redirect('/host/')

#数据删除
def test_delete(request):
	hostname= request.POST.get('hostname')
	print(hostname)
	models.Host.objects.filter(hostname=hostname,).delete()
	return HttpResponse('%s已经删除'%hostname)

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



#增加主机和业务的后台数据
def add_host_business(request):
	b_l = [
		{'caption':'运维部',},
		{'caption':'测试',},
		{'caption':'开发',},
		{'caption':'市场',},
	]
	for i in b_l:
		models.Business.objects.create(**i)
	for i in range(1,101):
		h_l = {'hostname':'beijing%s.cgpower.cn'%i,'ip':'192.168.1.%s'%i,'port':'8%s'%i,'b_id': 1,}
		models.Host.objects.create(**h_l)
	return HttpResponse('add  data OK')

