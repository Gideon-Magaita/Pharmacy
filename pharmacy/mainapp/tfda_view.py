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
@allowed_users(allowed_roles=['tfda'])
def tfda_home(request):
    return render(request,'pages/tfda/home.html')


@login_required(login_url='login_user')
@allowed_users(allowed_roles=['tfda'])
def tfda_applications(request):
    application = Applicant.objects.all()
    context={
        'application':application,
    }
    return render(request, 'pages/tfda/applications.html',context)




@login_required(login_url='login_user')
@allowed_users(allowed_roles=['tfda'])
def tfda_comment(request,id):
    application = Applicant.objects.get(id=id)
    form = TfdaForm(request.POST or None,instance=application)
    if form.is_valid():
        form.save()
        messages.success(request,'Details updated successfully')
        return redirect('tfda_applications')
    context={
        'form': form,
    }
    return render(request, 'pages/tfda/tfda-comment.html',context)





@login_required(login_url='login_user')
@allowed_users(allowed_roles=['tfda'])
def tfda_details(request,id):
    details = Applicant.objects.get(id=id)
    return render(request, 'pages/tfda/tfda-view-details.html',{'details':details})