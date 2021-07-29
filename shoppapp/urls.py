from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *


app_name = 'shoppapp'
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("products/", ProductsView.as_view(), name="products"),
    path("product/<int:pk>/<str:name>/details/", product_detail_view, name="product_details"),

    path("about/", AboutUsView.as_view(), name="about"),
    path("contact/", ContactUsView.as_view(), name="contact"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)