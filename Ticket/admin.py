from django.contrib import admin

# Register your models here.
from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
	list_display = ("title", "description", "image", "time_created")
	list_editable = ("time_created",)


admin.site.register(Ticket)
