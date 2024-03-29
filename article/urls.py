from django.urls import path
from .views import *

app_name = 'article'

urlpatterns = [
    
    path('', index , name= 'index'),

    path('article/<int:pk>/', single_article, name='single_article'), 

    path('article/category/<int:pk>/', categorised_article, name='categorised_article'),  

    path('article/post/', post_article, name= 'post_article'), 

    
]

