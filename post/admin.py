from django.contrib import admin
from .models import *

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BlogPost._meta.fields]
