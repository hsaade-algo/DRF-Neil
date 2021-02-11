from django.contrib import admin

from .models import Foo, FooBar
# Register your models here.

admin.site.register(Foo)
admin.site.register(FooBar)
