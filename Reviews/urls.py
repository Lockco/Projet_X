from django.urls import path
from .views import index, review_01, ReviewHome


app_name = "Reviews"

urlpatterns = [
	path('', ReviewHome.as_view(), name='home')
	#path("", index, name="review-index"),
	#path("review-<str:numero_review>", review_01, name="review-review-01.html")
]
