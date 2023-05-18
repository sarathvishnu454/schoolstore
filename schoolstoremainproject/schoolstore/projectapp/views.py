from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import message
from django.shortcuts import render, redirect
from .models import form
# Create your views here.
from .forms import NewUserForm


def home(request):
    return render(request, 'home.html')


def index1(request):
    return render(request, 'index.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration succesfull.")
            return redirect('login')
        messages.error(request, "unsuccesfull registration.Invalid information")
    form = NewUserForm
    return render(request=request, template_name='register.html', context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'you are now logged in as {username}.')
                return redirect("form")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def details(request):
    if request.method == "POST":
        name = request.POST.get("Name", )
        DOB = request.POST.get("DOB", )
        AGE = request.POST.get("Age", )
        GENDER = request.POST.get("Gender", )
        PHONENUMBER = request.POST.get("Phonenumber", )
        MAILID = request.POST.get("Mailid", )
        ADDRESS = request.POST.get("Address", )
        DEPARTMENT = request.POST.get("Department", )
        # COURSES = request.POST.get("Courses", )
        Purpose = request.POST.get("Purpose", )
        Materialsprovide = request.POST.get("Materialsprovide", )
        F = form(NAME=name, DOB=DOB, Age=AGE, Gender=GENDER, Phonenumber=PHONENUMBER, Mailid=MAILID, Address=ADDRESS,
                 Department=DEPARTMENT, Purpose=Purpose, Materialsprovide=Materialsprovide)
        F.save()
        messages.info(request, "registration successfull")
        return redirect('detail')


    return render(request, 'form.html')

def detail(request):
    return render(request, 'detail.html')

def logout_request(request):
    auth.logout(request)
    return redirect("login")
