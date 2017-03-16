#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from web.service import log

class LogListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'log_list.html')

class LogJsonView(View):

    def get(self, request):
        obj = log.Log()
        response = obj.fetch_log(request)
        return JsonResponse(response.__dict__)
    def delete(self, request):
        pass

    def put(self, request):
        pass




