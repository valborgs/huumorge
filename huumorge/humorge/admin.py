from django.contrib import admin
from .models import FreeBoard, HumorBoard, FreeComment, HumorComment
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class PostForm(admin.ModelAdmin):

    fieldsets = [
        ("author", {'fields': ["author"]}),
        ("Title/date", {'fields': ["title", "date"]}),
        ("Content", {"fields": ["content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(FreeBoard, PostForm)
admin.site.register(FreeComment)
admin.site.register(HumorBoard, PostForm)
admin.site.register(HumorComment)
