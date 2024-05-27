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



@login_required(login_url='login_user')
@allowed_users(allowed_roles=['weo'])
def weo_home(request):
    return render(request, 'pages/weo/home.html')



@login_required(login_url='login_user')
@allowed_users(allowed_roles=['weo'])
def weo_applications(request):
    application = Applicant.objects.all()
    context={
        'application':application,
    }
    return render(request, 'pages/weo/applications.html',context)



@login_required(login_url='login_user')
@allowed_users(allowed_roles=['weo'])
def weo_comment(request,id):
    application = Applicant.objects.get(id=id)
    form = WeoForm(request.POST or None,instance=application)
    if form.is_valid():
        form.save()
        messages.success(request,'Details updated successfully')
        return redirect('applications')
    context={
        'form': form,
    }
    return render(request, 'pages/weo/weo-comment.html',context)




@login_required(login_url='login_user')
@allowed_users(allowed_roles=['weo'])
def weo_details(request,id):
    details = Applicant.objects.get(id=id)
    return render(request, 'pages/weo/view-details.html',{'details':details})