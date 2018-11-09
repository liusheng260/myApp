from django.shortcuts import render,redirect

# Create your views here.
# coding:utf-8
from django.http import HttpResponse
from django.template import loader,Context
from .models import Vip
from django import forms
#from functools import wraps

# def index(request):
#     t = loader.get_template("index.html")
#     #c = Context({"title": "djangon"})
#     html=t.render({"title": "djangon"})
#     return HttpResponse(html)

# def add(request):
#     a=request.GET['a']
#     b=request.GET['b']
#     c=str(int(a)+int(b))
#     return HttpResponse(c)

class UserForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

def register(request):
    #t = loader.get_template("register.html")
    if request.method=="POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            re_username = uf.cleaned_data['username']
            re_password = uf.cleaned_data['password']
            db_username=Vip.objects.values_list('username',flat=True)
            db_password=Vip.objects.values_list('password',flat=True)
            for i in range(len(db_username)):
                if db_username[i]==re_username:
                    return redirect('/register/')
                        #return render(request,'share1.html',{'registerAdd':registerAdd,'username':username})
            else:
                registerAdd = Vip.objects.create(username=re_username,password=re_password)
                return render(request,'share1.html',{'registerAdd':registerAdd})
            # if registerAdd == False:
            #     return render(request,'share1.html',{'registerAdd':registerAdd,'username':username})
            # else:
            #     return render(request,'share1.html',{'registerAdd':registerAdd})
    else:
        uf = UserForm()
    return render(request,'register.html',{'uf':uf})


def index(request):
    t = loader.get_template("index.html")
    v1 = Vip.objects.all()
    html = t.render({"v1":v1})
    return HttpResponse(html)

def login(request):
    t = loader.get_template("login.html")
    if request.method=="POST":
        input_username=request.POST.get('username')
        input_password=request.POST.get('password')
        db_username=Vip.objects.values_list('username',flat=True)
        db_password=Vip.objects.values_list('password',flat=True)
        for i in range(len(db_username)):
            for j in range(len(db_password)):
                if db_username[i]==input_username and db_password[j]==input_password:
                    return redirect('/index/')
        else:
            return HttpResponse(t.render({'status':'ERROR Incorrect username or password'}))
    return HttpResponse(t.render())

def add(request):
    t = loader.get_template("add.html")
    return HttpResponse(t.render())