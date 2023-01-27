from django.urls import path
from reviews import views
from reviews.views import ReviewHome


app_name = "reviews"


urlpatterns = [
    path('',  views.feed, name='home'),
    path('feed/', views.feed, name='feed'),
    path('create/', views.create_review, name='create_review'),
    path('review_detail/<int:review_id>/', views.review_detail, name='review_detail'),
    path('reply_to_ticket/<str:ticket_id>', views.reply_to_ticket, name='reply_to_ticket')
]