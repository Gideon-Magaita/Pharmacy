from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups.all()[0].name=='applicant':
                return redirect('home')
            elif request.user.groups.all()[0].name=='cfdc':
                return redirect('cfdc_home')
            elif request.user.groups.all()[0].name=='tfda':
                return redirect('tfda_home')
            elif request.user.groups.all()[0].name=='veo':
                return redirect('veo_home')
            elif request.user.groups.all()[0].name=='weo':
                return redirect('weo_home')
            else:
                return view_func(request,*args, **kwargs)
        else: 
            return view_func(request,*args, **kwargs)
    return wrapper_func   

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None
            if request.user.groups.exists():
               group = request.user.groups.all()[0].name

            if group in allowed_roles:
               return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')   
        return wrapper_func
    return decorator 

def admin_only(view_func):
    def wrapper_func(request,*args, **kwargs):
        group = None
        if request.user.groups.exists():
           group = request.user.groups.all()[0].name
        if group == 'cfdc':
            return redirect('cfdc_home')
        if group == 'tfda':
            return redirect('tfda_home')
        if group == 'veo':
            return redirect('veo_home')
        if group == 'weo':
            return redirect('weo_home')
        if group == 'admins':
            return redirect('admin_home')
        if group == 'applicant':
            return view_func(request,*args, **kwargs)
    return wrapper_func        

