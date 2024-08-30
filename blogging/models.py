from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=128)
    # It is OK for the body of a post to be empty
    # TextFields are better when you do not know the length of the
    # entry
    text = models.TextField(blank=True)
    # Dango comes with a table for users, so we point the author to
    # the User table. CASCADE will delete all posts from a author
    # if that author is deleted from the Users table
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
