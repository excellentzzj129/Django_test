# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response

#表單
def search_form(request):
    return render_to_response('search_form.html')

#接收請求數據
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = '你搜索的內容爲：' + request.GET['q']
    else:
        message = '你提交了空表單'
    return HttpResponse(message)
