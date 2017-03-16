#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from web.service import tag

class TagListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tag_list.html')

class TagJsonView(View):

    def get(self, request):
        obj = tag.Tag()
        response = obj.fetch_tag(request)
        return JsonResponse(response.__dict__)
    def delete(self, request):
        pass

    def put(self, request):
        pass




