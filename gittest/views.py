#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2022-2-10 17:39
#@Author: yangjian
#@File  : views.py
from django.shortcuts import render

def index(request):
    return render(request,'index.html')