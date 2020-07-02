
from .import views
from django.urls import path



# 给视图函数定义访问路由
urlpatterns = [
    path('abc/', views.hello),
]
