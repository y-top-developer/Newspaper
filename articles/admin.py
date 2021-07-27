from articles.models import Article, Comment
from django.contrib import admin

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)