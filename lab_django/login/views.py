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
        message = '请填写用户名与密码！'
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
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        message = '请填写完用户名与密码并确认！'
        if username.strip() and password and password2:
            if password != password2:
                message = '两次输入的密码不一致！请重新确认'
                return render(request, 'login/register.html', {'message': message})
            else:
                exist_user = models.User.objects.filter(name=username) #从数据库中根据用户名检索是否已存在
                if exist_user:
                    message = '用户名已存在！请更换用户名。'
                    return render(request, 'login/register.html', {'message': message})

                new_user = models.User()
                new_user.name = username
                new_user.password = password
                new_user.save()
                message = '注册成功！'
                return render(request, 'login/login.html', {'message': message})#成功注册返回登录界面
        else:
            return render(request, 'login/register.html', {'message': message})
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect("/login/")