from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import render
from django.views.generic import ListView

from tickets.models import Ticket


class TicketHome(ListView):
	model = Ticket
	context_object_name = "tickets"


class TicketCreateForm(forms.Form):
	title = forms.CharField(max_length=128, label="Titre")
	description = forms.CharField(required=False, label="Déscription")
	image = forms.ImageField(required=False, label="Image")  # Ajout du champ pour l'image

	class Meta:
		model = Ticket
		exclude = ['ticket']
		fields = ['title', 'description', 'image', ]


@login_required(login_url='followers:login')
def create_ticket(request):
	if request.method == 'POST':
		form = TicketCreateForm(request.POST, request.FILES)
		if form.is_valid():
			# On crée un ticket
			ticket = Ticket.objects.create(
				title=form.cleaned_data['title'],
				description=form.cleaned_data['description'],
				user=request.user,
				image=form.cleaned_data['image']
			)
			ticket.save()
			return render(request, 'reviews/review_list.html')
	else:
		form = TicketCreateForm()
	return render(request, 'ticket_form.html', {'form': form})
