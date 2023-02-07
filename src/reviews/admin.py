from django.contrib import admin

# Register your models here.
from reviews.models import Review


class ReviewAdmin(admin.ModelAdmin):
	list_display = ("user", "headline", "body", "time_created")


admin.site.register(Review, ReviewAdmin)
