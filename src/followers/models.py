from django.contrib.auth.models import User
from django.db import models


class UserFollows(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
	followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed")
	time_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Follower'
		verbose_name_plural = 'Tous les followers'
		ordering = ["user"]
		unique_together = ('user', 'followed_user',)