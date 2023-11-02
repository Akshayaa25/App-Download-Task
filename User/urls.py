from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('userLogin',views.userLogin,name='userLogin'),
    path('userSignup',views.userSignup,name='userSignup'),
    path('logout',views.logout,name='logout'),
    path('userProfile',views.userProfile,name='userProfile'),
    path('userDashboard',views.userDashboard,name='userDashboard'),
    path('taskCompleted',views.taskCompleted,name='taskCompleted'),
    path('taskAssigned',views.taskAssigned,name='taskAssigned'),
    path('taskDetails/<int:id>',views.taskDetails,name='taskDetails'),
    path('screenShot/<int:id>',views.screenShot,name='screenshot'),
]