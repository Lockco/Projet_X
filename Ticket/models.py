from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Ticket(models.Model):
	title = models.CharField(max_length=128)
	description = models.TextField(max_length=2048, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField
	time_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Ticket'
		verbose_name_plural = 'Tous les Tickets'
		ordering = ["user"]

	def __str__(self):
		return f"{self.title}-{self.time_created}"

	@property
	def publish_string(self):
		if self.title:
			return "l'article est disponible"
		else:
			return "l'article n'est pas disponible"

	def save(self, *args, **kwargs):

		super().save(*args, **kwargs)
