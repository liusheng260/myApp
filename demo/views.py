from django.shortcuts import render,redirect

# Create your views here.
# coding:utf-8
from django.http import HttpResponse
from django.template import loader,Context
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
import time
# from .models import Article
from django import forms
from functools import wraps
#说明：这个装饰器的作用，就是在每个函数视图被调用时，都验证下有没有登录
#如果登录则调用新的视图函数，
#否则没有登录则自动跳转到登录页面
def check_login(f):
    @wraps(f)
    def inner(request,*arg,**kwargs):
        if request.session.get('is_login')=='1':
            return f(request,*arg,**kwargs)
        else:
            return redirect('/login/')
    return inner

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

def login(request):
    t = loader.get_template("login.html")
    if request.method=="POST":
        input_username=request.POST.get('username')
        input_password=request.POST.get('password')
        # db_username=Vip.objects.values_list('username',flat=True)
        # db_password=Vip.objects.values_list('password',flat=True)
        #user = Vip.objects.get(username = request.POST['username'])
        user = Vip.objects.filter(username = input_username,password = input_password)
        print(user)
        if user:
        #判断是否查询成功
        # for i in range(len(db_username)):
        #     for j in range(len(db_password)):
        #         if db_username[i]==input_username and db_password[j]==input_password:
            request.session['is_login']='1'
            request.session['Vip_username'] = user[0].username
            return redirect('/index/')
        # else:
    #return HttpResponse(t.render({'status':'ERROR Incorrect username or password'}))

        # if user.password == request.POST['password']:
        #     request.session['Vip_id'] = user.id
        #     return HttpResponse("You're logged in.")
        # else:
        #     return HttpResponse("Your username and password didn't match.")
           
        # if db_username[i]==input_username:
        #     if user.password == request.POST['password']:
        #         request.session['Vip_id'] = user.id
        #         return redirect('/index/')
        #     else:
        #         return HttpResponse("Your username and password didn't match.")

    return HttpResponse(render(request,'login.html'))

@check_login
def index(request):
    art = Article.objects.all().order_by('-lastchange')[:5]
    Vip_username1 = request.session.get('Vip_username')
    userobj=Vip.objects.filter(username=Vip_username1)
    if userobj:
        return render(request,'index.html',{"users":userobj[0],"art":art})
    else:
        return render(request,'index.html',{'users':'匿名用户',"art":art})

def logout(request):
    try:
        del request.session['Vip_username']
        print(request.session.get('Vip_username'))
    except KeyError:
        pass
    return HttpResponse(render(request,'login.html'))

@check_login
def add(request):
    name1=Vip.objects.filter(username=request.session.get('Vip_username'))
    name = name1[0]
    print(name)
    if request.method=="POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        category = request.POST.get('category')
        blogAdd = Article.objects.create(title=title,body=body,category=category,autho=name,slug=time.time())
        return HttpResponse(render(request,'myblog.html',{"users":name}))
    else:
        return HttpResponse(render(request,'add.html',{"users":name}))   

@check_login
def about(request):
    Vip_username1 = request.session.get('Vip_username')
    userobj=Vip.objects.filter(username=Vip_username1)
    print(userobj)
    if userobj:
        return render(request,'about.html',{"users":userobj[0]})
    else:
        return render(request,'about.html',{'users':'匿名用户'})

@check_login
def myblog(request):
    Vip_username1 = request.session.get('Vip_username')
    userobj=Vip.objects.filter(username=Vip_username1)
    blog_title = Article.objects.all()
    print(userobj)
    print(blog_title)
    if userobj:
        return render(request,'myblog.html',{"users":userobj[0],'tt':blog_title})
    else:
        return render(request,'myblog.html',{'users':'匿名用户','tt':blog_title})

@check_login
def detail(request):
    art = Article.objects.all().order_by('-lastchange')[:5]
    id = request.GET.get("id")
    Vip_username1 = request.session.get('Vip_username')
    userobj=Vip.objects.filter(username=Vip_username1)
    blog_body = Article.objects.filter(id=id).values()
    cm = Article.objects.all()
    # blogAdd = Article.objects.create(title=title,body=body,category=category,autho=name,slug=time.time())
    body = blog_body[0]
    if userobj:
        return render(request,'detail.html',{'users':userobj[0],'bd':body,'art':art})
    else:
        return render(request,'detail.html',{'users':'匿名用户','bd':body,'art':art})