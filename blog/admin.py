from django.contrib import admin
from .models import BlogPost, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "color"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ["name"]}


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ["title", "published", "published_at", "views", "created_at"]
    list_filter = ["published", "tags"]
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ["title"]}
    date_hierarchy = "published_at"
    readonly_fields = ["views", "created_at", "updated_at", "published_at"]
    filter_horizontal = ["tags"]
