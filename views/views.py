#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

reload(sys)
sys.setdefaultencoding('utf-8')


def default(req):
	return HttpResponse("欢迎来到 程序猿世界 ！！！")
	
def hello(req):
	context = {}
	context['username'] = "程序猿"
	return render(req, 'hello.html', context)
	
def search_form(req):
	return render_to_response('search_form.html')
	
def search(req):
	req.encoding='utf-8'
	if req.method == 'GET' and 'query' in req.GET:
		msg = '你搜索的内容为：'+req.GET['query']
	else:
		msg = '你提交了空表单'
	return HttpResponse(msg)