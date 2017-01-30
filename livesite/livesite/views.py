# coding:utf-8
from django.shortcuts import render_to_response,render
from .forms import RegisterForm,LoginForm,ChangepwdForm,ApplyForm,UpdateLiveInfoForm
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required  
from .models import UserProfile
import json

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def login_validate(request,username,password):
    rtvalue = False
    user = authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            auth_login(request,user)
            return True
    return rtvalue

def register(request):
    error=[]
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            email = data['email']
            password = data['password']
            password2 = data['password2']
            if not User.objects.all().filter(username=username):
                if not User.objects.all().filter(email=email):
                    if form.pwd_validate(password, password2):
                        user = User.objects.create_user(username, email, password)
                        user.save()
                        login_validate(request,username,password)
                        UserProfile.objects.create(user = user)
                        return HttpResponseRedirect('/index/')
                    else:
                        error.append('Please input the same password')
                else:
                    error.append('The email has existed,please use forget password')
            else:
                error.append('The username has existed,please change your username')
    else:
        form = RegisterForm()   
    return render_to_response('register.html',{'form':form,'error':error})

def mylogin(request):
    error = []
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            if login_validate(request,username,password):
                return HttpResponseRedirect('/index/')
            else:
                error.append('Please input the correct password')
        else:
            error.append('Please input both username and password')
    else:
        form = LoginForm()
    return render_to_response('login.html',{'error':error,'form':form})

def mylogout(request):
    auth_logout(request)
    return HttpResponseRedirect('/index/')

def changepassword(request,username):  
    error = []  
    if request.method == 'POST':  
        form = ChangepwdForm(request.POST)  
        if form.is_valid():  
            data = form.cleaned_data  
            user = authenticate(username=username,password=data['old_password'])  
            if user is not None:  
                if data['new_password']==data['new_password2']:  
                    newuser = User.objects.get(username__exact=username)  
                    newuser.set_password(data['new_password'])  
                    newuser.save()  
                    return HttpResponseRedirect('/login/')  
                else:  
                    error.append('Please input the same password')  
            else:  
                error.append('Please correct the old password')  
        else:  
            error.append('Please input the required domain')  
    else:  
        form = ChangepwdForm()  
    return render_to_response('changepassword.html',{'form':form,'error':error})  

@login_required  
def apply(request):
    error = []  
    if request.method == 'POST': 
        form = ApplyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data     
            current_user = request.user
            user_profile_set = UserProfile.objects.filter(user = current_user)
            if user_profile_set[0]:
                user_profile = user_profile_set[0]
                if user_profile.status == 'default':
                    user_profile_set.update(id_card = data['id_card'],title = data['title'],describe = data['describe'],status = u'apply')
                    return HttpResponseRedirect('/applydone/')
                elif user_profile.status == 'apply':
                    error.append('You have already apply,you cant apply again, please wait')
                    #return HttpResponseRedirect('/applydone/')
                elif user_profile.status == 'ok':
                    error.append('You have ')
            else:
                error.append('There may have some trouble of user')
    else:  
        form = ApplyForm()  
    return render_to_response('apply.html',{'form':form,'error':error})  
# Create your views here.

def applydone(request):
    return render(request, 'applydone.html',{})

def playlistjson(request):
    user_profile_set = UserProfile.objects.filter(status = 'ok').filter(switch = 'open')
    response_data = {}
    if user_profile_set:  
        playlist = []
        
        for userprofile in user_profile_set:
            playitem = {}
            playitem['title'] = userprofile.title
            playitem['name'] = userprofile.user.username
            playitem['describe'] = userprofile.describe
            playitem['play_url'] = userprofile.play_url
            playitem['websocket_url'] = userprofile.websocket_url
            playlist.append(playitem)
        
        if playlist:
            response_data['status'] = 'success'
            response_data['playlist'] = playlist
        else:
            response_data['status'] = 'failed'
    return HttpResponse(json.dumps(response_data), content_type="application/json")  

def updateliveinfo(request):
    error = []  
    if request.method == 'POST':
        form = UpdateLiveInfoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data 
            current_user = request.user
            user_profile_set = UserProfile.objects.filter(user = current_user)
            if user_profile_set[0]:
                user_profile_set.update(title=data['title'],describe = data['describe'],switch = data['switch'])    
                return HttpResponse("update done")
    else:  
        form = UpdateLiveInfoForm()  
    return render_to_response('updateliveinfo.html',{'form':form,'error':error})  