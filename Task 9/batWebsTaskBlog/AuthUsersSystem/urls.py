"""
URL configuration for batWebsTaskBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import UserRegisterView, UserEditView, ChangePasswordView, ProfileView, EditProfileView, CreateProfileView
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edituser/', UserEditView.as_view(), name='edit-user'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password/', ChangePasswordView.as_view()),
    path('password_changed/', views.password_changed,name='password_changed'),
    path('<int:pk>/profile/', ProfileView.as_view(),name='profile'),
    path('<int:pk>/editprofile/', EditProfileView.as_view(),name='edit-profile'),
    path('createprofile/', CreateProfileView.as_view(),name='create-profile'),
]
