from django.http import HttpResponse
from django.template import loader

from .models import Post

# Create your views here.
def news(request):
    myposts = Post.objects.all().values()
    template = loader.get_template('news.html')
    context = {
        'myposts': myposts,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  mypost = Post.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mypost': mypost,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())