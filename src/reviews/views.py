from django.shortcuts import render, get_object_or_404, redirect
from followers.models import UserFollows
from reviews.models import Review
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.db.models import CharField, Value, Q
from tickets.models import Ticket
from django import forms

from tickets.views import TicketCreateForm


class ReviewHome(ListView):
    model = Review
    context_object_name = "reviews"


class ReviewCreate(CreateView):
    model = Review
    templates_name = "reviews/create_review.html"
    fields = ['title','rating', 'headline', 'body']


class ReviewCreateForm(forms.ModelForm):
    headline = forms.CharField(max_length=128)
    body = forms.CharField(required=False)
    RATING_CHOICES = [(i, str(i)) for i in range(0, 6)]
    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=RATING_CHOICES)
    image = forms.ImageField(required=False)

    class Meta:
        model = Review
        exclude = ['ticket']
        fields = ['headline', 'body', 'rating', ]


@login_required(login_url='followers:login')
def create_review(request):
    if request.method == 'POST':
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            # On crée un ticket
            ticket = Ticket.objects.create(
                title=form.cleaned_data['headline'],
                description=form.cleaned_data['body'],
                user=request.user,
                image=form.cleaned_data['image']
            )
            ticket.save()
            # On récupère le dernier ID de ticket
            last_ticket_id = Ticket.objects.filter(user=request.user).last().id
            # On crée la critique en réponse au ticket créé
            review = Review.objects.create(
                ticket_id=last_ticket_id,
                rating=form.cleaned_data['rating'],
                user=request.user,
                headline=form.cleaned_data['headline'],
                body=form.cleaned_data['body'],
            )
            return render(request, 'reviews/review_list.html')
    else:
        form = ReviewCreateForm()
    return render(request, 'reviews/create_review.html', {'form': form})


@login_required(login_url='followers:login')
def reply_to_ticket(request, ticket_id):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except Ticket.DoesNotExist:
        return redirect('reviews:home')
    if request.method == 'POST':
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('reviews:home')
    else:
        form = ReviewCreateForm()
    return render(request, 'reviews/reply_to_ticket.html', {'form': form, 'ticket': ticket})


@login_required(login_url='followers:login')
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {'review': review}
    return render(request, 'reviews/review_detail.html', context)


@login_required(login_url='followers:login')
def get_users_viewable_reviews(request):
    # Récupération des avis de l'utilisateur connecté
    user_reviews = Review.objects.filter(user=request.user)
    # Récupération des utilisateurs que l'utilisateur connecté suit
    followed_users = UserFollows.objects.filter(user=request.user).values_list('followed_user', flat=True)
    # Récupération des avis des utilisateurs que l'utilisateur connecté suit
    followed_users_reviews = Review.objects.filter(user__in=followed_users)
    # Union des deux querysets
    reviews = user_reviews | followed_users_reviews
    return reviews

@login_required(login_url='followers:login')
def get_users_viewable_tickets(request):
    # Récupération des utilisateurs que l'utilisateur connecté suit
    followed_users = UserFollows.objects.filter(user=request.user).values_list('followed_user', flat=True)
    # Récupération des tickets de l'utilisateur connecté et des utilisateurs qu'il suit
    tickets = Ticket.objects.filter(Q(user=request.user) | Q(user__in=followed_users))
    return tickets


@login_required(login_url='followers:login')
def feed(request):
    reviews = get_users_viewable_reviews(request)
    # returns queryset of reviews
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    tickets = get_users_viewable_tickets(request)
    # returns queryset of tickets
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    # if not posts:
    #     return render(request, 'reviews/feed.html', context={'message': "Vous n'avez rien publié"})

    return render(request, 'reviews/feed.html', context={'posts': posts})

@login_required(login_url='followers:login')
def user_posts(request):
    reviews = Review.objects.filter(user=request.user)
    tickets = Ticket.objects.filter(user=request.user)
    context = {'reviews': reviews, 'tickets': tickets}
    return render(request, 'review_list.html', context)

@login_required(login_url='followers:login')
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewCreateForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews:user_posts')
    else:
        form = ReviewCreateForm(instance=review)
    return render(request, 'edit_review.html', {'form': form})


@login_required(login_url='followers:login')
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    return redirect('reviews:user_posts')


@login_required(login_url='followers:login')
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if request.method == 'POST':
        form = TicketCreateForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('user_posts')
    else:
        form = TicketCreateForm(instance=ticket)
    return render(request, 'edit_ticket.html', {'form': form})


@login_required(login_url='followers:login')
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    ticket.delete()
    return redirect('user_posts')