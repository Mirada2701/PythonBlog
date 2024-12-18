from django.urls import include, path
from . import views

app_name = 'posts'

urlpatterns = [
    
    path('', views.news, name='news'),
    path('details/<int:id>', views.details, name='details'),

]

