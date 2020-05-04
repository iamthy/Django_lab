from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        return redirect('/index/')
    return render(request, 'login/login.html')


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect("/login/")