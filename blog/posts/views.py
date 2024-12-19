from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Post

# Create your views here.
def news(request):
    posts = Post.objects.all()
    return render(request, "news.html", {'posts': posts})

def details(request, id):
  mypost = Post.objects.get(id=id)
  return render(request,"details.html",{'mypost':mypost})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  
            post.created_by = request.user   
            post.save()   
            return redirect('posts:news')
    else:
        form = forms.PostForm()
    return render(request, 'posts/post_form.html', {'form': form})
