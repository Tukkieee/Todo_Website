from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home-page'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout', views.logoutButton, name='logout'),
    path('delete-task/<int:id>/', views.DeleteTask, name='delete'),
    path('complete-task/<int:id>/', views.CompleteTask, name='complete'),
    path('edit-task/<int:id>/', views.EditTask, name='edit'),
    path('clear-all-tasks/', views.DeleteAllTask, name='clear'),



]
