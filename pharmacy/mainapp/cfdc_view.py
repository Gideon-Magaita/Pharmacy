from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
#authentication imports
from django.contrib.auth.models import Group
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users,admin_only



@login_required(login_url='login_user')
@allowed_users(allowed_roles=['cfdc'])
def cfdc_home(request):
    return render(request,'pages/cfdc/home.html')



@login_required(login_url='login_user')
@allowed_users(allowed_roles=['cfdc'])
def cfdc_applications(request):
    application = Applicant.objects.all()
    context={
        'application':application,
    }
    return render(request, 'pages/cfdc/applications.html',context)




@login_required(login_url='login_user')
@allowed_users(allowed_roles=['cfdc'])
def cfdc_comment(request,id):
    application = Applicant.objects.get(id=id)
    form =CfdcForm(request.POST or None,instance=application)
    if form.is_valid():
        form.save()
        messages.success(request,'Details updated successfully')
        return redirect('cfdc_applications')
    context={
        'form': form,
    }
    return render(request, 'pages/cfdc/cfdc-comment.html',context)





@login_required(login_url='login_user')
@allowed_users(allowed_roles=['cfdc'])
def cfdc_view_details(request,id):
    details = Applicant.objects.get(id=id)
    return render(request, 'pages/cfdc/view-application.html',{'details':details})
