from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages

def home(request):
    return render(request,'home.html',{})
def display(request):
    studs = Student.objects.all
    return render(request,'display.html',{'studs' : studs})
def webform(request):
    if request.method == "POST":
        form = StudentForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,('Data Submitted'))
            return redirect('display')
        else:
            messages.success(request,('Error! Try Again.'))
            return render(request,'webform.html',{})
    else:
        return render(request,'webform.html',{})