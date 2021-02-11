from django.db import models
from django.contrib.auth.models import User


class Foo(models.Model):
    class Meta:
        verbose_name_plural = "Foo"
    
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class FooBar(models.Model):
    class Meta:
        verbose_name_plural = "FooBar"
    
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
