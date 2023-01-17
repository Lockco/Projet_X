from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from itertools import chain

import collections

from Reviews.models import Review
from Tickets.models import Ticket


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    followers = models.ManyToManyField('self', related_name='following', symmetrical=False)
    tickets_created = models.ManyToManyField(Ticket, related_name='tickets_created')
    reviews_created = models.ManyToManyField(Review, related_name='reviews_created')
    is_active = models.BooleanField(default=True)

    def follow(self, user):
        self.followers.add(user)

    def unfollow(self, user):
        self.followers.remove(user)

    def get_stream(self):
        tickets = self.tickets_created.all()
        reviews = self.reviews_created.all()
        following_tickets = Ticket.objects.filter(user__in=self.followers.all())
        following_reviews = Review.objects.filter(user__in=self.followers.all())
        return list(chain(tickets, reviews, following_tickets, following_reviews))
    
    USERNAME_FIELD = 'email'


class UserFollows(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed")
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'followed_user', )


