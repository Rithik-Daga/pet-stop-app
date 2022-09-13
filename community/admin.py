from . import models
from django.contrib import admin


class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "user_comment"]
    list_filter = ["post", "user"]
    list_per_page = 50


# Register your models here.
admin.site.register(models.Comments, CommentAdmin)
