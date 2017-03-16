#!/usr/bin/env python
# -*- coding:utf-8 -*-
from io import BytesIO
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from utils.check_code import create_validate_code
from django.core.exceptions import ValidationError
from repository import models

from web.forms import LoginForm
import json


class JsonCustomEncoder(json.JSONEncoder):
    def default(self, field):
        if isinstance(field, ValidationError):
            return {'code':field.code,'message':field.messages}
        else:
            return json.JSONEncoder.default(self, field)


def check_code(request):
    """
    验证码
    :param request:
    :return:
    """
    stream = BytesIO()
    img, code = create_validate_code()
    img.save(stream, 'PNG')
    request.session['CheckCode'] = code
    return HttpResponse(stream.getvalue())


def login(request):
    """
    登陆
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        e = request.POST.get('email')
        t = models.UserInfo.objects.filter(username=u)
        ret = {'status': True, 'error': None, 'data': None,}
        # obj = LoginForm()
		#
        # if obj.is_valid():
        #     print(obj.cleaned_data)
        # else:
        #     ret['error'] = obj.errors.as_data()
        #     result = json.dumps(ret,cls=JsonCustomEncoder)
        #     print(result)
        #     return HttpResponse(result)
        ##当用户不存在时，返回login登陆界面
        if not t:
            return render(request, 'login.html')
        else:
            obj = models.UserInfo.objects.get(username=u)
        # 当密码正确时，进入跳转到'/backend_base_info.html'这个url，并且增加一个cookie
        if obj.password == p:
            request.session['username'] = u
            request.session['is_login'] = True
            if request.POST.get('rmb', None) == '1':
                # 设置免登陆超时时间5秒
                request.session.set_expiry(5)
                return redirect('/backend/base-info.html')
            # 不设置免登陆时间默认是两周
            return redirect('/backend/base-info.html')
        else:
            return render(request, 'login.html')


    #
    # if request.method == 'GET':
    #     return render(request,'login.html')
    # elif request.method == "POST":
    #     obj = LoginForm(request.POST)
	#
    #     if obj.is_valid():
    #         print(obj.cleaned_data)
    #     else:
    #         ret['error'] = obj.errors.as_data()
    #         result = json.dumps(ret,cls=JsonCustomEncoder)
    #         print(result)
    #         return HttpResponse(result)

	#
    #     if request.session['CheckCode'].upper() == request.POST.get('check_code').upper():
    #         pass
    #     else:
    #         print('验证码错误')
	#
	#
    # return render(request, 'login.html')


def register(request):
    """
    注册
    :param request:
    :return：
    """
    return render(request, 'register.html')


def logout(request):
    """
    注销
    :param request:
    :return:
    """
    pass
