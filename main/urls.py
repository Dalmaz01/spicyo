from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('about', views.about_page, name='about_page'),
    path('blog', views.blog_page, name='blog_page'),
    path('contact', views.contact_page, name='contact_page'),
    path('index', views.index_page, name='index_page'),
    path('recipe', views.recipe_page, name='recipe_page'),
    path('foods', views.foods_page, name='foods_page'),
]