from django.http import Http404
from django.shortcuts import render,get_object_or_404
from main import models

# Create your views here.
def index(request):
    latest_articles = models.Article.objects \
    .all() \
    .order_by('-createdAt')[:10]
    context = {
        "latest_articles" : latest_articles
    }
    return render(request,'main/index.html',context)

def article(request,pk):
    # try :
    #     article = models.Article.objects.get(pk = pk) # pk => primary key
    # except :
    #     raise Http404()
    article = get_object_or_404(models.Article,pk=pk)
    context = {
        "article" : article
    }
    return render(request,'main/article.html',context)

def author(request,pk):
    author = get_object_or_404(models.Author,pk=pk)
    context = {
        "author" : author
    }
    return render(request,'main/author.html',context)
