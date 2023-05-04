from django.contrib import admin

from .models import Article, Journalist

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["author", "title",]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Journalist)
