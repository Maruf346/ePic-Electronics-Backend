from django.contrib import admin
from .models import Project, ProjectStat, ProjectSection


class ProjectStatInline(admin.TabularInline):
    model = ProjectStat
    extra = 1
    fields = ["value", "label", "order"]


class ProjectSectionInline(admin.StackedInline):
    model = ProjectSection
    extra = 1
    fields = ["heading", "text", "image", "image_alt", "order"]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "category",
        "featured",
        "created_at",
    ]
    list_filter = ["category", "featured"]
    search_fields = ["title", "description", "category"]
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Basic Information", {
            "fields": (
                "title", "short_title", "slug", "description",
                "image", "content", "category", "featured"
            ),
        }),
        ("Detailed Content", {
            "fields": ("introduction",),
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )

    inlines = [ProjectStatInline, ProjectSectionInline]