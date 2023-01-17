from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


class User(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
	followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_by')

	class META:
		unique_together = ('user', 'followed_user')
		verbose_name = 'Utilisateur'
		verbose_plural_name = 'Tous les Utilisateurs'

	def __str__(self):
		return f"{self.user}-{self.followed_user}"

	@property
	def user_string(self):
		if self.user:
			return "l'utilisateur est disponible"
		else:
			return "l'utilisateur n'est pas disponible"

	def save(self, *args, **kwargs):

		super().save(*args, **kwargs)
