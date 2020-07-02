from django.shortcuts import render
from django.http import HttpResponse   #导入HttpResponse

# Create your views here.

# 定义视图函数，输出hello world
# 定义的视图函数必须有参数，request为所有请求对象
def hello(request):
    # 返回响应字符
    # return HttpResponse("Hello World")

    # 返回响应模板
    return render(request,"hello.html")


# 最后异步重新启动服务
#











