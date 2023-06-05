from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import ArticleForm
from .models import Article
# Create your views here.

def article_search_view(request):
  query = request.GET.get("q")
  qs = Article.objects.search(query)
  context = {
     "object_list": qs
  }
  return render(request, "articles/search.html", context=context)

@login_required
def article_create_view(request):
    # print(request.POST)
    form = ArticleForm(request.POST or None)
    context = {
       "form": form
    }
    if form.is_valid():
      article_object = form.save()
      # title = form.cleaned_data.get("title")
      # content = form.cleaned_data.get("content")
      # # print(title, content)
      # article_object = Article.objects.create(title=title, content=content)
      context["object"] = article_object
      context["created"] = True
      return redirect(article_object.get_absolute_url())
    return render(request, "articles/create.html", context=context)

# def article_create_view(request):
#     # print(request.POST)
#     form = ArticleForm()
#     context = {
#        "form": form
#     }
#     if request.method == "POST":
#       form = ArticleForm(request.POST)
#       if form.is_valid():
#          title = form.cleaned_data.get("title")
#          content = form.cleaned_data.get("content")
#          print(title, content)
#          article_object = Article.objects.create(title=title, content=content)
#          context["object"] = article_object
#          context["created"] = True
#     return render(request, "articles/create.html", context=context)

def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
      try:
         article_obj = Article.objects.get(slug=slug)
      except Article.DoesNotExist:
         raise Http404
      except Article.MultipleObjectsReturned:
         article_obj = Article.object.filter(slug=slug).first()
      except:
         raise Http404
    context = {
        "object": article_obj
    }
    return render(request, "articles/detail.html", context=context)