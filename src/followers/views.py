from django.contrib import auth
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from followers.forms import CustomUserChangeForm, FollowForm
from followers.models import UserFollows


def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('reviews:home')
	else:
		form = UserCreationForm()
	return render(request, 'followers/signup.html', {'form': form})


def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				auth.login(request, user)
				return redirect('reviews:home')
	form = AuthenticationForm()
	return render(request, 'followers/login.html', {'form': form})


@login_required
def profile(request):
	if request.method == 'POST':
		form = CustomUserChangeForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('followers:profile')
	else:
		form = CustomUserChangeForm(instance=request.user)
	return render(request, 'followers/profile.html', {'form': form})


@login_required(login_url='followers:login')
def logout_view(request):
	logout(request)
	return redirect('reviews:home')


@login_required(login_url='followers:login')
def follow_user(request):
	if request.method == 'POST':
		form = FollowForm(request.POST)
		if form.is_valid():
			followed_username = form.cleaned_data['username']
			try:
				followed_user = User.objects.get(username=followed_username)
				follow = UserFollows(user=request.user, followed_user=followed_user)
				follow.save()
				return redirect('followers:follow')
			except User.DoesNotExist:
				form.add_error('username', 'Utilisateur non trouvé')
	else:
		form = FollowForm()
	follows = UserFollows.objects.filter(user=request.user)
	follow_by = UserFollows.objects.filter(followed_user_id=request.user.id)
	print(follow_by)
	followed_users = [follow.followed_user for follow in follows]
	return render(request, 'followers/follow_form.html',
	              {'followed_users': followed_users, 'form': form, 'follow_by': follow_by}
	              )


@login_required
def unfollow(request, user_id):
	user_to_unfollow = User.objects.get(pk=user_id)
	request.user.follower.filter(followed_user=user_to_unfollow).delete()
	return redirect('followers:follow')
