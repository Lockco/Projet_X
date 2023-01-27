from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class CustomUserChangeForm(UserChangeForm):
	# Redefining fields
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-class'}), label="Nom d'utilisateur")
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-class'}), label="Nom")
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-class'}), label="Prénom")
	password = forms.CharField(widget=forms.PasswordInput(), label="Mot de passe")
	# Adding new fields
	age = forms.IntegerField()
	bio = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = User
		fields = ["username", "email"]


class FollowForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-class'}), label="Nom d'utilisateur")
