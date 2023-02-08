from django.views.generic import ListView, DetailView
from .models import Product, Category


class ProductsList(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'

# dfv
# ate your views here.
