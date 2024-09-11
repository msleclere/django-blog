from django.contrib import admin
from django.db import models
from blogging.models import Post, Category


class CategroyAdmin(admin.ModelAdmin):
    exclude = ('posts',)


class CategoryInLine(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInLine, ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategroyAdmin)
