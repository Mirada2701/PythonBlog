from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from .models import Post

# Create your views here.
@login_required(login_url='users:login')
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

