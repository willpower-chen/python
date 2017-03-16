#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from web.service import business

class BusinessListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'business_list.html')

class BusinessJsonView(View):

    def get(self, request):
        obj = business.Business()
        response = obj.fetch_business(request)
        # return HttpResponse(json.dumps(response.__dict__))
        return JsonResponse(response.__dict__)
    def delete(self, request):
        pass

    def put(self, request):
        pass




