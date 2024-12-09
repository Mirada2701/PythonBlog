from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.main, name='main'),
    path('news/', views.news, name='news'),
    path('news/details/<int:id>', views.details, name='details'),

]

