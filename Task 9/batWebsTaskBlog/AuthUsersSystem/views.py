from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import RegistrationForm, EditUserForm, ChangePasswordForm, EditProfileForm, CreateProfileForm
from BlogDemo.models import Category,UserProfile
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class UserRegisterView(SuccessMessageMixin, generic.CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    success_message = "Registered successfully!"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.filter(id__lte=5)
        context = super(UserRegisterView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class UserEditView(SuccessMessageMixin, generic.UpdateView):
    form_class = EditUserForm
    template_name = 'registration/edit_user.html'
    success_url = reverse_lazy('home')
    success_message = "Info updated successfully!"

    def get_object(self):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.filter(id__lte=5)
        context = super(UserEditView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    form_class = ChangePasswordForm
    template_name='registration/change_password.html'
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('password_changed')
    success_message = "Password changed successfully!"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.filter(id__lte=5)
        context = super(ChangePasswordView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

def password_changed(request):
    cat_menu = Category.objects.filter(id__lte=5)
    return render(request,'registration/password_changed.html',{'cat_menu':cat_menu})

class ProfileView(generic.DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = UserProfile.objects.all()
        cat_menu = Category.objects.filter(id__lte=5)
        context = super(ProfileView,self).get_context_data(*args,**kwargs)
        profile_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context["cat_menu"] = cat_menu
        context["profile_user"] = profile_user
        return context
    
class EditProfileView(SuccessMessageMixin, generic.UpdateView):
    model = UserProfile
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    # fields = ['profile_pic','bio','website_url','social_media_url']
    success_url = reverse_lazy('home')
    success_message = "Profile updated successfully!"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.filter(id__lte=5)
        context = super(EditProfileView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
    
class CreateProfileView(SuccessMessageMixin, generic.CreateView):
    model = UserProfile
    form_class = CreateProfileForm
    template_name = 'registration/create_profile.html'
    # fields = '__all__'
    success_url = reverse_lazy('home')
    success_message = "Profile created successfully!"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.filter(id__lte=5)
        context = super(CreateProfileView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context