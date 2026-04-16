from django.contrib import admin
from .models import Profile, Skill, Timeline


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "email", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["name", "title", "email"]
    readonly_fields = []


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "order"]
    list_filter = ["category"]
    search_fields = ["name"]
    ordering = ["order", "name"]


@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    list_display = ["title", "organization", "start_date", "end_date", "is_education"]
    list_filter = ["is_education", "is_ongoing"]
    search_fields = ["title", "organization"]
    ordering = ["-start_date"]
