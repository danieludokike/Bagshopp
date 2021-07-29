from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import (
    ListView, TemplateView,
    DetailView,
)
from django.contrib.auth.views import (
    LoginView,
)

from .models import (
    Product
)


class HomeView(ListView):
    template_name = "shoppapp/index.html"
    model = Product
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


class ProductsView(TemplateView):
    template_name = "shoppapp/products.html"
    pass


class AboutUsView(TemplateView):
    template_name = "shoppapp/about.html"
    pass


class ContactUsView(TemplateView):
    template_name = "shoppapp/contact.html"
    pass


def product_detail_view(request, pk, name):
    template = "shoppapp/product_details.html"
    product = get_object_or_404(Product, id=pk)
    products = Product.objects.all()
    context = {
        "product": product,
        "products": products,
        "name": name,
    }
    return render(request, template, context)

#
# def user_registration(request):
#     """HANDLES USER REGISTRATION"""
#     template
