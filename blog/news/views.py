from django.http import HttpResponse
from django.template import loader

from .models import News

# Create your views here.
def news(request):
    mynews = News.objects.all().values()
    template = loader.get_template('news.html')
    context = {
        'mynews': mynews,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  mynews = News.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mynews': mynews,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())