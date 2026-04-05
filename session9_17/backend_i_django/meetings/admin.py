# backend_i_django/meetings/admin.py
from django.contrib import admin
from .models import Meeting, ActionItem


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "date", "owner")
    list_filter = ("date", "owner")
    search_fields = ("title", "owner")


@admin.register(ActionItem)
class ActionItemAdmin(admin.ModelAdmin):
    list_display = ("id", "meeting", "owner", "due_date", "status")
    list_filter = ("status", "owner", "due_date")
    search_fields = ("description", "owner")

    # Challenge: custom admin action para marcar tasks como completed
    @admin.action(description="Marcar selecionados como completed")
    def mark_completed(self, request, queryset):
        queryset.update(status="completed")

    actions = ["mark_completed"]
