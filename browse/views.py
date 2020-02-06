from django.shortcuts import render,redirect
from django.http import  HttpResponse,HttpResponseRedirect
# Create your views here.
from .forms import LoginForm, SignupForm
from .models import File
from django.contrib.auth.models import User
from django.contrib import auth
files = File.objects.all()


def index(request):
    """if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['user'] == "sanju" and form.cleaned_data['pas'] == 'root':
                return HttpResponseRedirect('/sanju')

    form = LoginForm()
    """
    return render(request, 'browse/index.html', {'files': files, 'parent': 0})


def item(request):
    g = request.GET['id']
    it = files.filter(id=g)
    return render(request, 'browse/index.html', {'g': g, 'files': it, 'parent': 1})


def login(request):
    if request.method == "GET":
        return render(request,'browse/login.html')
    if request.method == "POST":
        form  = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['user'],password=form.cleaned_data['pas'])
            if user is not None:
                auth.login(request,user)
                return redirect('index')
            else:
                return render(request,'browse/login.html',{'error':'username of password incorrect'})
        else:
            return render(request,'browse/index.html')


def logout(request):
    if request.method =="POST":
        auth.logout(request)
        return  redirect('index')



def signup(request):
    if request.method == "GET":
        return render(request,'browse/signup.html')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                u = User.objects.get(username=form.cleaned_data['user'])
                return render(request,'browse/signup.html',{'error':"Username already exists"})
            except User.DoesNotExist:
                user = User(username=form.cleaned_data['user'])
                user.set_password(form.cleaned_data['pas'])
                print(form.cleaned_data['last'])
                user.save()
                auth.login(request,user)
                return redirect('index')
        return render(request,'browse/signup.html',{'error':"Try again"})