from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "created_at", "read", "replied"]
    list_filter = ["read", "replied"]
    search_fields = ["name", "email", "message"]
    readonly_fields = ["created_at"]
    date_hierarchy = "created_at"

    actions = ["mark_as_read", "mark_as_replied"]

    def mark_as_read(self, request, queryset):
        queryset.update(read=True)

    mark_as_read.short_description = "Mark selected messages as read"

    def mark_as_replied(self, request, queryset):
        queryset.update(replied=True)

    mark_as_replied.short_description = "Mark selected messages as replied"
