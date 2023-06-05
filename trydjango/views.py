"""
To render html web pages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from articles.models import Article

def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    name = "Will"
    random_id = random.randint(1, 3)
    # from the database??
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }

    # Django Templates

    # tmpl = get_template("home-view.html")
    # tmpl_string = tmpl.render(context=context)

    HTML_STRING = render_to_string("home-view.html", context=context)
    # HTML_STRING = """
    # <h1>{title} ({id})!</h1>
    # <p>{content}</p>
    # """.format(**context)

    return HttpResponse(HTML_STRING)
