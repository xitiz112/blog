from django.urls import path
from . import views
from account.views import SignupView,profile
from django.contrib.auth import views as auth_views

urlpatterns=[
#path("",views.index, name='blog home'),
 path ('signup/' , SignupView.as_view(),name='signup'),
 path ('login/' ,auth_views.LoginView.as_view(template_name='account/login.html'),name='login'),
 path ('logout/' , auth_views.LogoutView.as_view(template_name='account/logout.html'),name='logout'),
 path ('profile/' ,views.profile,name='profile'),
]