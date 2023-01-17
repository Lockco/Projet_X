from django.contrib import admin

# Register your models here.
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
	list_display = ("ticket", "rating", "user", "headline", "body", "time_created")
	list_editable = ("time_created",)


admin.site.register(Review)
