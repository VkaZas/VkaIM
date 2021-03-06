"""VkaIM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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

from django.views.static import serve

from VkaIM import settings
from account import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', views.visit_register, name='vis_register'),
    url(r'^login/$', views.visit_login, name='vis_login'),
    url(r'^register/register.do', views.do_register, name='do_register'),
    url(r'^login/login.do', views.do_login, name='do_login'),
    # url(r'^vkazas/$', views.echo_once)
    url(r'^common_static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
