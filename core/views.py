from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from django.contrib import messages
from blog.models import Post
# Create your views here.

from .forms import LoginForm, NewUserForm


def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'core/frontpage.html', {'posts' : posts})


def aboutpage(request):
    return render(request, 'core/about.html')

def loginpage(request):
    form= LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )

            if user is not None:
                login(request,user)
                message = f'Hello {user.username}! Log in is successful!'
                messages.success(request, message)
                return redirect('/')
            else:
                message = 'Login failed, check your email and password!'
                messages.error(request, message)
            
    return render(request, 'core/login.html', {'form':form, 'message':message})    

def registerpage(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="core/register.html", context={"register_form":form})