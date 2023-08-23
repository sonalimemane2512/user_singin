

from django.contrib import admin
from django.urls import path
from login import views
from signin import settings


urlpatterns = [
    path('loginuser/', views.LoginUser, name="loginuser"),
    path('homepage', views.HomePage, name="homepage"),
    path('logout/', views.LogoutUser, name="logout"),
    path('clicklogin', views.clicklogin, name="clicklogin"),
    path('register_user/', views.RegisterUser, name="register_user"),
    path('click_user', views.ClickRegister, name="click_user"),
    path('', views.RegisterUser, name=""),
    path('admin/', admin.site.urls),
]