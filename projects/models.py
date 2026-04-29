from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    CATEGORY_CHOICES = [
        ("Power Supply", "Power Supply"),
        ("Embedded", "Embedded"),
        ("IoT", "IoT"),
        ("PCB Design", "PCB Design"),
        ("Automation", "Automation"),
        ("Other", "Other"),
    ]

    title = models.CharField(max_length=300)
    short_title = models.CharField(max_length=150, blank=True)
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/")
    content = models.TextField(help_text="Short overview content")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    featured = models.BooleanField(default=False)

    # Detailed content
    introduction = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectStat(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="stats"
    )
    value = models.CharField(max_length=50)
    label = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Project Stat"
        verbose_name_plural = "Project Stats"

    def __str__(self):
        return f"{self.label}: {self.value}"


class ProjectSection(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="sections"
    )
    heading = models.CharField(max_length=300)
    text = models.TextField()
    image = models.ImageField(upload_to="projects/sections/", blank=True, null=True)
    image_alt = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Project Section"
        verbose_name_plural = "Project Sections"

    def __str__(self):
        return f"{self.project.title} - {self.heading}"