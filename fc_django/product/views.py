from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = "product.html"  # 2개만 적어도 리스트뷰 생성끝
    context_object_name = 'product_list'  # html 참조변수명 선언 default : object_list
