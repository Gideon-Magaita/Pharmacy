from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.http import JsonResponse
#authentication imports
from django.contrib.auth.models import Group
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users,admin_only



@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'username or password is incorrect') 

    return render(request,'pages/auth/login.html')



def logoutUser(request):
    logout(request)
    return redirect('login_user')



@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
           user = form.save()
           username = form.cleaned_data.get('username')
           group = Group.objects.get(name='applicant')
           user.groups.add(group)
           messages.success(request, 'Account was created for '+ username)
           return redirect('login_user')
    else:
        form = CreateUserForm()    
    return render(request,'pages/auth/register.html',{'form':form})




#-----home---function----------

@login_required(login_url='login_user')
@admin_only
def home(request):
    return render(request,'pages/applicant/home.html')



@login_required(login_url='login_user')
@admin_only
def request_permit(request):
    application = Applicant.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Application submitted!')
            return redirect('request_permit')
        else:
            messages.error(request,'Something went wrong')
            return redirect('request_permit')
    else:
        form = ApplicationForm()
    context={
        'form': form,
        'application':application,
    }
    return render(request,'pages/applicant/request_permit.html',context)




@login_required(login_url='login_user')
@admin_only
def edit_permit(request,id):
    permit = Applicant.objects.get(id=id)
    form = ApplicationForm(request.POST or None,request.FILES or None,instance=permit)
    if form.is_valid():
        form.save()
        messages.success(request,'Application updated!')
        return redirect('request_permit')
    context={
        'form': form,
    }
    return render(request,'pages/applicant/edit-permit.html',context)




@login_required(login_url='login_user')
@admin_only
def delete_permit(request,id):
    permit = Applicant.objects.get(id=id)
    permit.delete()
    messages.success(request,'Application deleted!')
    return redirect('request_permit')




    