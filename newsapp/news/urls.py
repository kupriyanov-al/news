from django.urls import path
from .views import NewsView, NewsDetail 


urlpatterns = [
  
    path('', NewsView.as_view(), name='news_list'),
    path('<int:pk>/', NewsDetail.as_view(), name='news_detail')

]
