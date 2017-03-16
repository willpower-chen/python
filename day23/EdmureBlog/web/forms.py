#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/

from django import forms
from django.forms import fields
from django.forms import widgets

class LoginForm(forms.Form):
	username = fields.CharField(
		required=True,
		error_messages={'required':"用户不能为空"}
	)
	password = fields.CharField(
		max_length=64,
		min_length=12,
		error_messages={'max_length':'密码长度不能大于64'}
	)