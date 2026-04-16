from django.contrib import admin
from .models import Project, ProjectTag


@admin.register(ProjectTag)
class ProjectTagAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "color"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ["name"]}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "featured", "created_at"]
    list_filter = ["featured", "technologies"]
    search_fields = ["title", "description"]
    prepopulated_fields = {"slug": ["title"]}
    readonly_fields = ["created_at"]
    filter_horizontal = ["technologies"]
