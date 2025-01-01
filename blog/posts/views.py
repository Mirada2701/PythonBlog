from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Post

# Create your views here.
@login_required
def office(request):
    posts = Post.objects.filter(created_by=request.user)
    return render(request, 'office.html', {'posts':posts}) 

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

@login_required
def edit(request, id):
  post = Post.objects.get(id=id)
  if request.method == 'POST':
     form = forms.PostForm(request.POST, request.FILES, instance=post)
     if form.is_valid():
        form.save()
        return redirect('posts:office')
  else:
        form = forms.PostForm(instance=post)
  return render(request, 'posts/post_form.html', {'form': form})

@login_required
def post_delete(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:office')
