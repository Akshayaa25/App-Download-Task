from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('adminLogin',views.adminLogin,name='adminLogin'),
    path('adminSignup',views.adminSignup,name='adminSignup'),
    path('logout',views.logout,name='logout'),
    path('adminDashboard',views.adminDashboard,name='adminDashboard'),
    path('addApps',views.addApps,name='addApps')
]

