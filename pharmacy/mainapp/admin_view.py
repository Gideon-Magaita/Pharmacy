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
@allowed_users(allowed_roles=['admins'])
def admin_home(request):
    return render(request, 'pages/admins/home.html')



@login_required(login_url='login_user')
@allowed_users(allowed_roles=['admins'])
def users(request):
    users = User.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            group = form.cleaned_data['group']

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            else:
                user = User.objects.create_user(username=username, password=password)
                group.user_set.add(user)
                messages.success(request, 'User added successfully.')

            return redirect('users')
    else:
        form = UserForm()
    
    return render(request, 'pages/admins/manage-users.html', {'form': form,'users':users})



@login_required(login_url='login_user')
@allowed_users(allowed_roles=['admins'])
def delete_user(request,id):
    futa_user = User.objects.get(id=id)
    futa_user.delete()
    messages.success(request,'user deleted')
    return redirect('users')
