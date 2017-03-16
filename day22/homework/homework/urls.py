"""homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from cmdb import  views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^adb/$', views.add_host_business),
    url(r'^business/$', views.business),
    url(r'^host/$', views.host),
    url(r'^test_ajax$', views.test_ajax),
    url(r'^test_delete$', views.test_delete),
    url(r'^ajax_submit_edit$', views.ajax_submit_edit),
    url(r'^app$', views.app),
    url(r'^app_ajax_add$', views.app_ajax_add),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^cache/$', views.cache),
    url(r'^fm/$', views.fm),
]
