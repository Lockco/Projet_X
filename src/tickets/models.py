from django.db import models


# Create your models here.


class Ticket(models.Model):
	title = models.CharField(max_length=128)
	description = models.TextField(max_length=2048, blank=True)
	user = models.ForeignKey('users.user', on_delete=models.CASCADE)
	image = models.ImageField
	time_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Ticket'
		verbose_name_plural = 'Tous les tickets'
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
