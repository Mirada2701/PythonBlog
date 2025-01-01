from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post

def main(request):
    return render(request,"main.html")