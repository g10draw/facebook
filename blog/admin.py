from django.contrib import admin

from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'text')

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)