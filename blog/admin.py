from django.contrib import admin
from blog.models import Blog
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'number_views', 'published')
    search_fields = ('title',)
    list_filter = ('published', 'created_at')
    ordering = ('created_at',)