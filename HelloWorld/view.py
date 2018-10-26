#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Torre Yang Edit with Python3.6
# @Email  : klyweiwei@163.com
# @Time   : 2018/10/26 17:18

# from django.http import HttpResponse  # render 可以替换
from django.shortcuts import render


def hello(request):
    context = dict()
    context['hello'] = 'Hello world hello'
    context['athletes'] = ['torre', 'janet']
    return render(request, 'hello.html', context)

