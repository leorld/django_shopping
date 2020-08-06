from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm

# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = "product.html"  # 2개만 적어도 리스트뷰 생성끝
    context_object_name = 'product_list'  # html 참조변수명 선언 default : object_list


class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'
