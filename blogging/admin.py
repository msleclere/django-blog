from django.contrib import admin
from django.db import models
from blogging.models import Post, Category

admin.site.register(Category)


# admin.site.register(Post)

class CategoryInLine(admin.StackedInline):
    model = Category
    exclude = ('posts',)


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInLine, ]


admin.site.register(Post, PostAdmin)
