"""myApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from demo import views as learn_views

urlpatterns = [
    #url(r'^$', learn_views.index),
    #path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^add/$', learn_views.add),
    url(r'^login/$', learn_views.login),
    url(r'^index/$', learn_views.index),
    url(r'^register/$', learn_views.register),
    url(r'^about/$', learn_views.about),
]
