from django.shortcuts import render
from django.views.generic import ListView

from Reviews.models import Review


# Create your views here.
def index(request):
	return render(request, "review/index.html")


def review_01(request, numero_review):
	return render(request, f"review/review-{numero_review}.html")


class ReviewHome(ListView):
	model = Review
	context_object_name = "Reviews"
