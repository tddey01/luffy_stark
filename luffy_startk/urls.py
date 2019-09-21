"""luffy_startk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url, include
from app01.views import index
from kn import site

print('在路由读取前打印信息', site._registry)

print('路由加载')
urlpatterns = [
    url(r'^web/' ,site.urls )
]

'''
    web/index/ ---> index
    web/home/  --->  home
    
    
    
  urlpatterns = [
    # url('admin/', admin.site.urls),
    path(r'^web/',  (urlconf_module, app_name, namespace)),
]  
   
 '''
