from django.shortcuts import render
from django.shortcuts import redirect
from . import models
# Create your views here.


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username.strip() and password:
            try:
                user = models.User.objects.get(name=username)#从数据库中根据用户名检索
            except:
                message = '用户名不正确！'
                return render(request, 'login/login.html', {'message': message})#没有这个用户就返回登录界面
            if (user.password == password): # 有的话还要检查密码是否正确
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', {'message': message})
        else:
            return render(request, 'login/login.html', {'message': message})
    return render(request, 'login/login.html')


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect("/login/")