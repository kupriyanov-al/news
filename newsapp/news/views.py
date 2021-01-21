from django.shortcuts import render
from .models import Category, News
from django.views.generic.list  import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse
# Create your views here.

class NewsView(ListView):
    model = News
    context_object_name = 'news_list'
    template_name = 'news_list.html'

class NewsDetail(DetailView):
    model = News
    # context_object_name = 'news_list'
    # template_name = 'news_list.html'
    context_object_name = 'news_list'
    template_name = 'news_detail.html'

class NewsCategoryView(ListView):
    model = News
    context_object_name = 'news_list'
    template_name = 'news_list.html'
    
    
    def get_queryset(self):
        return News.objects.filter(category__pk=self.kwargs['pk'])


