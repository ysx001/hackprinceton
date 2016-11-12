from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles import views

urlpatterns = [
    url(r'^$', include('myproject.myapp.urls')),
    ]  + static(settings.MEDIA_URL)

