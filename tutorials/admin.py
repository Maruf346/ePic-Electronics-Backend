from django.contrib import admin
from .models import Tutorial, TutorialSection


class TutorialSectionInline(admin.StackedInline):
    model = TutorialSection
    extra = 1
    fields = ["heading", "text", "image", "image_alt", "order"]


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "created_at"]
    list_filter = ["category"]
    search_fields = ["title", "description", "category"]
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Basic Information", {
            "fields": (
                "title", "slug", "description",
                "image", "content", "category"
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

    inlines = [TutorialSectionInline]