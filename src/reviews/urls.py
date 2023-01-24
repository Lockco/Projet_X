from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from reviews import views
from reviews.views import ReviewHome, ReviewCreate

app_name = "reviews"


urlpatterns = [
    path('', ReviewHome.as_view(), name='home'),
    path('feed/', views.feed, name='feed'),
    path('create/', views.create_review, name='create_review'),
    path('review_detail/<int:review_id>/', views.review_detail, name='review_detail'),
]