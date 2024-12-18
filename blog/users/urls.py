from django.urls import include, path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('home/', views.home_page, name='home'),
    path('', include('posts.urls')),

]