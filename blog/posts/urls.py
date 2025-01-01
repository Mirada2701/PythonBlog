from django.urls import include, path
from . import views

app_name = 'posts'

urlpatterns = [
    
    path('', views.news, name='news'),
    path('office', views.office, name='office'),
    path('details/<int:id>', views.details, name='details'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('post/new/', views.post_create, name='create'),
    path('delete/<int:id>/', views.post_delete, name='delete'),
]

