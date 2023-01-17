from django.shortcuts import get_object_or_404, redirect
from User.models import User

def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    request.user.followers.add(user_to_follow)
    return redirect('user_profile', user_id=user_id)

def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    request.user.followers.remove(user_to_unfollow)
    return redirect('user_profile', user_id=user_id)
