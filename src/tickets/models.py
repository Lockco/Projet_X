from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Ticket(models.Model):
	title = models.CharField(max_length=128)
	description = models.TextField(max_length=2048, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(blank=True, upload_to='cover')
	time_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Ticket'
		verbose_name_plural = 'Tous les tickets'
		ordering = ["user"]

	def __str__(self):
		return f"{self.title}-{self.time_created}"