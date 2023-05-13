from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('message/<str:pk>/', views.viewMessage, name="message"),
    path('create-message/', views.createMessage, name="create-message"),
]
