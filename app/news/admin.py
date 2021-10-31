from django.contrib import admin
from .models import *
from django.db.models import fields


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'creation_date', 'author_name', 'votes']
    list_filter = ['creation_date']

@admin.register(Comments)
class CommetsAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'content', 'creation_date']
    list_filter = ['creation_date']