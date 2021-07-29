from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shoppapp.urls')),

    # DJANGO AUTHENTICATION URLS CONF
    path("account/", include("django.contrib.auth.urls")),
    # DJANGO FLUTTERWAVE URLS CONF
    path("djangoflutterwave/", include("djangoflutterwave.urls", namespace="djangoflutterwave"))

]
