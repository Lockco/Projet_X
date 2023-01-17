from django.contrib import admin

# Register your models here.
from .models import User


class UserAdmin(admin.ModelAdmin):
	list_display = ("user", "followed_user")
	list_editable = ("user",)


admin.site.register(User)
