from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models
from itertools import chain


class User(AbstractBaseUser):
	email = models.EmailField(unique=True)
	nom = models.CharField(max_length=255)
	prenom = models.CharField(max_length=255)
	date_naissance = models.DateField()
	followers = models.ManyToManyField('self', related_name='following', symmetrical=False, blank=True)
	tickets_created = models.ManyToManyField("tickets.ticket", related_name='tickets_created', blank=True)
	reviews_created = models.ManyToManyField("reviews.review", related_name='reviews_created', blank=True)
	is_active = models.BooleanField(default=True)
	password = models.CharField(max_length=128)

	class Meta:
		verbose_name = 'Utilisateur'
		verbose_name_plural = 'Toutes les utilisateurs'
		ordering = ["nom"]

	def save(self, *args, **kwargs):
		if not self.tickets_created:
			self.tickets_created = []
		if not self.reviews_created:
			self.reviews_created = []
		super().save(*args, **kwargs)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['nom', 'prenom', 'date_naissance', 'password']

	objects = UserManager()

	def __str__(self):
		return self.email

	def add(self, email, nom, prenom, date_naissance):
		self.email = email
		self.nom = nom
		self.prenom = prenom
		self.date_naissance = date_naissance
		self.save()

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.is_admin

	# # def follow(self, user):
	# #     self.followers.add(user)

	# # def unfollow(self, user):
	# #     self.followers.remove(user)

	# # def get_stream(self):
	# #     tickets = self.tickets_created.all()
	# #     reviews = self.reviews_created.all()
	# #     following_tickets = "tickets.ticket".objects.filter(user__in=self.followers.all())
	# #     following_reviews = "reviews.review".objects.filter(user__in=self.followers.all())
	# #     return list(chain(tickets, reviews, following_tickets, following_reviews))

	USERNAME_FIELD = 'email'


class UserFollows(models.Model):
	user = models.ForeignKey("users.user", on_delete=models.CASCADE, related_name="follower")
	followed_user = models.ForeignKey("users.user", on_delete=models.CASCADE, related_name="followed")
	time_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('user', 'followed_user',)
