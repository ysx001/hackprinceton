# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf.urls.static import static
from myproject.myapp.views import index

urlpatterns = [
    url(r'^$', index, name = 'index')
]