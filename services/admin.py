from django.contrib import admin
from .models import (
    Service,
    ServiceProvideItem,
    ServiceProblem,
    ServiceStat,
    ServiceStep,
    ServiceCapability,
)


class ServiceProvideItemInline(admin.TabularInline):
    model = ServiceProvideItem
    extra = 1
    fields = ["text", "order"]


class ServiceProblemInline(admin.TabularInline):
    model = ServiceProblem
    extra = 1
    fields = ["title", "description", "order"]


class ServiceStatInline(admin.TabularInline):
    model = ServiceStat
    extra = 1
    fields = ["value", "label", "order"]


class ServiceStepInline(admin.StackedInline):
    model = ServiceStep
    extra = 1
    fields = ["step", "title", "description", "icon", "order"]


class ServiceCapabilityInline(admin.TabularInline):
    model = ServiceCapability
    extra = 1
    fields = ["text", "order"]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "created_at"]
    list_filter = ["category"]
    search_fields = ["title", "description", "category"]
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Basic Information", {
            "fields": (
                "title", "short_title", "slug", "description",
                "hero_subtitle", "content", "image",
                "cta", "cta_secondary", "category"
            ),
        }),
        ("Intro Section", {
            "fields": ("intro_heading", "intro_subheading", "intro_content"),
        }),
        ("What We Provide", {
            "fields": ("what_we_provide_heading",),
        }),
        ("Problems We Solve", {
            "fields": ("problems_we_solve_heading",),
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )

    inlines = [
        ServiceProvideItemInline,
        ServiceProblemInline,
        ServiceStatInline,
        ServiceStepInline,
        ServiceCapabilityInline,
    ]