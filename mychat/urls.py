from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Define urlpatterns as an empty list
urlpatterns = []

# Add URL patterns for admin and your app
urlpatterns += [
    path('admin/', admin.site.urls),
    path('', include('videochat.urls')),  # Include the URLs from your app
]

# Add staticfiles_urlpatterns at the end
urlpatterns += staticfiles_urlpatterns()

