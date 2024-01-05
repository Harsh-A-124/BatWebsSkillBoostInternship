from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm,SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request,'home.html',{})
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You've Been Logged In!")
            return redirect('display')
        else:
            messages.success(request,('Error Logging In! Try Again.'))
            return redirect('login')
    else:
        return render(request,'login.html',{})
def logout_user(request):
    logout(request)
    messages.success(request,"You've Been Logged Out!")
    return redirect('login')

def display(request):
    if request.user.is_authenticated:
        studs = Student.objects.all()
        return render(request,'display.html',{'studs' : studs})
    else:
        messages.success(request,('You Must Be Logged In To View This Page!'))
        return redirect('login')
def webform(request):
    form = StudentForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request,('Record Added!'))
                return redirect('display')
            else:
                messages.success(request,('Error! Try Again.'))
                return redirect('webform')
        else:
            return render(request,'webform.html',{})
    else:
        messages.success(request,('You Must Be Logged In To View This Page!'))
        return redirect('login')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You've Successfully Registered! Welcome!")
			return redirect('login')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def student_record(request,pk):
    if request.user.is_authenticated:
        studs_record = Student.objects.get(id=pk)
        return render(request,'record.html',{'studs' : studs_record})
    else:
        messages.success(request,('You Must Be Logged In To View This Page!'))
        return redirect('login')
    
def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_rec = Student.objects.get(id=pk)
        delete_rec.delete()
        messages.success(request,('Record Deleted Successfully!'))
        return redirect('display')
    else:
        messages.success(request,('You Must Be Logged In To View This Page!'))
        return redirect('login')
    
# def add_record(request):
#     form = StudentForm(request.POST or None)
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             if form.is_valid():
#                 add_record = form.save()
#                 messages.success(request, "Record Added!")
#                 return redirect('home')
#         return render(request, 'add.html', {'form':form})
#     else:
#         messages.success(request,('You Must Be Logged In To View This Page!'))
#         return redirect('login')
    
def update_record(request,pk):
    curr_rec = Student.objects.get(id=pk)
    form = StudentForm(request.POST or None, instance=curr_rec)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request,('Record Updated!'))
                return redirect('display')
            else:
                messages.success(request,('Error! Try Again.'))
                return redirect('update')
        else:
            return render(request,'update.html',{'curr' : curr_rec})
    else:
        messages.success(request,('You Must Be Logged In To View This Page!'))
        return redirect('login')