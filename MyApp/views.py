from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.

@login_required
def welcome(request):
    return render(request, 'welcome.html',{"username": '123'})


def case_list(request):
    return render(request, 'welcome.html')

@login_required
def home(request):
    return render(request,'welcome.html', {"whichHTML": "Home.html","oid": ""})


def child(request, eid, oid):
    return render(request, eid)


def login(request):
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")

def login_action(request):
    u_name = request.GET.get('username')
    p_word = request.GET.get('password')
    user = auth.authenticate(username=u_name, password=p_word)
    if user is not None:
        auth.login(request, user)
        request.session['user'] = u_name
        return HttpResponse("成功")
    else:
        return HttpResponse("失败")


def register_action(request):
    u_name = request.GET.get('username')
    p_word = request.GET.get('password')
    try:
        user = User.objects.create_user(username=u_name,password=p_word)
        user.save()
        return HttpResponse("注册成功")
    except:
        return HttpResponse("注册失败")

