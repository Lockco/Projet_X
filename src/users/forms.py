from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	nom = forms.CharField(max_length=255, required=True)
	prenom = forms.CharField(max_length=255, required=True)
	date_naissance = forms.DateField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "nom", "prenom", "date_naissance", "password1", "password2")

	def save(self, commit=True):
		user = super().save(commit=False)
		user.email = self.cleaned_data["email"]
		user.nom = self.cleaned_data["nom"]
		user.prenom = self.cleaned_data["prenom"]
		user.date_naissance = self.cleaned_data["date_naissance"]
		if commit:
			user.save()
		return user
