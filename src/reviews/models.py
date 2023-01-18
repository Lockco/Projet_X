from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
	ticket = models.ForeignKey("tickets.ticket", on_delete=models.CASCADE)
	rating = models.PositiveIntegerField(max_length=None, validators=[MinValueValidator(0), MaxValueValidator(5)])
	user = models.ForeignKey("users.user", on_delete=models.CASCADE)
	headline = models.CharField(max_length=128)
	body = models.TextField(max_length=8192, blank=True)
	time_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Review'
		verbose_name_plural = 'Toutes les reviews'
		ordering = ["time_created"]

	def __str__(self):
		return f"{self.user}-{self.time_created}"

	@property
	def ticket_string(self):
		if self.time_created:
			return "l'article est disponible"
		else:
			return "l'article n'est pas disponible"

	def save(self, *args, **kwargs):

		super().save(*args, **kwargs)
