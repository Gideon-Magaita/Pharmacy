from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .import veo_view
from .import weo_view 
from .import cfdc_view
from .import tfda_view
from .import admin_view


urlpatterns=[
    path('',views.home,name='home'),
    path('request_permit',views.request_permit,name='request_permit'),
    path('edit_permit/<int:id>',views.edit_permit,name='edit_permit'),
    path('delete_permit/<int:id>',views.delete_permit,name='delete_permit'),
    #veo urls
    path('veo_home',veo_view.veo_home,name='veo_home'),
    path('applications',veo_view.applications,name='applications'),
    path('veo_comment/<int:id>',veo_view.veo_comment,name='veo_comment'),
    path('view_details/<int:id>',veo_view.view_details,name='view_details'),
    #weo urls
    path('weo_home',weo_view.weo_home,name='weo_home'),
    path('weo_applications',weo_view.weo_applications,name='weo_applications'),
    path('weo_comment/<int:id>',weo_view.weo_comment,name='weo_comment'),
    path('weo_details/<int:id>',weo_view.weo_details,name='weo_details'),
    #cfdc urls
    path('cfdc_home',cfdc_view.cfdc_home,name='cfdc_home'),
    path('cfdc_applications',cfdc_view.cfdc_applications,name='cfdc_applications'),
    path('cfdc_comment/<int:id>',cfdc_view.cfdc_comment,name='cfdc_comment'),
    path('cfdc_view_details/<int:id>',cfdc_view.cfdc_view_details,name='cfdc_view_details'),
    #tfda urls
    path('tfda_home',tfda_view.tfda_home,name='tfda_home'),
    path('tfda_applications',tfda_view.tfda_applications,name='tfda_applications'),
    path('tfda_comment/<int:id>',tfda_view.tfda_comment,name='tfda_comment'),
    path('tfda_details/<int:id>',tfda_view.tfda_details,name='tfda_details'),
    #admin urls
    path('admin_home',admin_view.admin_home,name='admin_home'),
    path('users',admin_view.users,name='users'),
    path('delete_user/<int:id>',admin_view.delete_user,name='delete_user'),
    #authenticationurls
    path('login_user',views.login_user,name='login_user'),
    path('register',views.register,name='register'),
    path('logoutUser',views.logoutUser,name='logoutUser'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)