from django.urls import path
from tickets import views
from tickets.views import TicketHome


app_name = "tickets"


urlpatterns = [
    path('ticket/', TicketHome.as_view(), name='ticket_snippet'),
    path('edit-ticket/', views.create_ticket, name='edit-ticket'),
]