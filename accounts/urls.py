from django.urls import path
from .import views

urlpatterns=[
    path('register',views.register,name='register'),
    path('login',views.login1,name='login1'),
    path('LogOut',views.LogOut,name='LogOut')

]