#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/

from django import template
from django.utils.safestring import mark_safe
# 创建register（register名字不能改）对象，
register = template.Library()
# simple_tag装饰器，多个参数
@register.simple_tag
def func1(a1,a2,a3):
	return a1 + a2
# filter装饰器只能两个参数
@register.filter
def func2(a1,a2):
	a2=a2.split(',')
	return a1,a2