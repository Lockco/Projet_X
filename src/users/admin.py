from django.contrib import admin

# Register your models here.
from users.models import User


class UserAdmin(admin.ModelAdmin):
	list_display = ("email", "nom", "prenom", "date_naissance", "is_active"  )
	


admin.site.register(User, UserAdmin)
