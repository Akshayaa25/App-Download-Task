from django.urls import path
from . import views

urlpatterns = [
    path('api/list/admin/', views.AdminList.as_view()),
    path('api/list/user/', views.UserList.as_view()),
    path('api/create/admin/', views.CreateAdmin.as_view()),
    path('api/create/user/', views.CreateUser.as_view()),
    path('api/create/app/', views.CreateApp.as_view()),
    path('api/list/app/', views.AppList.as_view()),
    path('api/tasks/completed/<str:username>/', views.TaskCompletedByUser.as_view()),
    path('api/task/details/<int:id>/', views.TaskDetails.as_view()),
]