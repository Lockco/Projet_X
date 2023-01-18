from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm


def signup(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			login(request, user)
			return redirect('users:profile')
	else:
		form = CustomUserCreationForm()
	return render(request, 'users/signup.html', {'form': form})


def login(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			user = authenticate(email=email, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Vous êtes connecté en tant que {email}")
				return redirect('users:profile')
			else:
				messages.error(request, "Invalid email or password.")
		else:
			messages.error(request, "Invalid email or password.")
	form = AuthenticationForm()
	return render(request, 'users/login.html', {'form': form})


def profile(request):
	user = request.user
	tickets = user.tickets_created.all()
	reviews = user.reviews_created.all()
	following = user.following.all()
	followers = user.follower.all()
	return render(request, 'users/profile.html',
	              {'ticket_created': tickets, 'reviews': reviews, 'following': following, 'followers': followers})
