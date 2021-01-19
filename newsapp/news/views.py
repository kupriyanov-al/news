from django.shortcuts import render
from .models import Category, News
from django.views.generic.list  import ListView

# Create your views here.

class NewsView(ListView):
    model = Category
    context_object_name = 'category'
    template_name = 'news_list.html'