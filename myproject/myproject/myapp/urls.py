# -*- coding: utf-8 -*-
from django.conf.urls import url
from myproject.myapp.views import index

urlpatterns = [
    url(r'^$', index, name = 'index')
]
