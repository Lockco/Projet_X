from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from LITReview import settings

urlpatterns = [
              path("admin/", admin.site.urls),
              path("", include('reviews.urls')),
              path('followers/', include('followers.urls')),
          ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
