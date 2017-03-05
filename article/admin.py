from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display=("block","article_title","article_status")

admin.site.register(Article,ArticleAdmin)