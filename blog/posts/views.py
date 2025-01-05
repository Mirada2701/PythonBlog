from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
@login_required
def office(request):
    posts = Post.objects.filter(created_by=request.user)
    return render(request, 'office.html', {'posts':posts}) 

def news(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "news.html", {'posts': posts, 'page_obj': page_obj})

def details(request, id):
  mypost = Post.objects.get(id=id)
  return render(request,"details.html",{'mypost':mypost})

@login_required
def post_create(request):
    posts = Post.objects.filter(created_by=request.user)
    if request.method == 'POST':
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  
            post.created_by = request.user   
            post.save()   
            return redirect('posts:news')
    else:
        form = forms.PostForm()
    return render(request, 'posts/post_form.html', {'form': form, 'is_edit':False, 'user_posts':posts})

@login_required
def edit(request, id):
  post = Post.objects.get(id=id)
  posts = Post.objects.filter(created_by=request.user)
  if request.method == 'POST':
     form = forms.PostForm(request.POST, request.FILES, instance=post)
     if form.is_valid():
        form.save()
        return redirect('posts:office')
  else:
        form = forms.PostForm(instance=post)
  return render(request, 'posts/post_form.html', {'form': form, 'is_edit':True, 'user_posts':posts})

@login_required
def post_delete(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:office')
