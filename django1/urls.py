"""django1 URL Configuration

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
from django.urls import path,include



# 需要在根部路由中配置当前应用的路由
# path（）和re_path（）的区别，
# re_path（）可以使用正则规则进行访问
urlpatterns = [
    path('admin/', admin.site.urls),   #默认的火箭页面
    path("",include("home.urls"))
]



# 最后一步启动服务
# python manage.py runserver
# 浏览器访问
