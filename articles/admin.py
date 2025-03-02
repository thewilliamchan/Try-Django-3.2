from django.contrib import admin

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'slug','timestamp', 'last_updated']
    search_fields = ['title']

admin.site.register(Article, ArticleAdmin)
