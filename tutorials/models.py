from django.db import models
from django.utils.text import slugify


class Tutorial(models.Model):
    CATEGORY_CHOICES = [
        ("PCB Design", "PCB Design"),
        ("Embedded Systems", "Embedded Systems"),
        ("Power Electronics", "Power Electronics"),
        ("IoT", "IoT"),
        ("Programming", "Programming"),
        ("Other", "Other"),
    ]

    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="tutorials/")
    content = models.TextField(help_text="Short overview content")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    # Detailed content
    introduction = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Tutorial"
        verbose_name_plural = "Tutorials"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class TutorialSection(models.Model):
    tutorial = models.ForeignKey(
        Tutorial, on_delete=models.CASCADE, related_name="sections"
    )
    heading = models.CharField(max_length=300)
    text = models.TextField()
    image = models.ImageField(upload_to="tutorials/sections/", blank=True, null=True)
    image_alt = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Tutorial Section"
        verbose_name_plural = "Tutorial Sections"

    def __str__(self):
        return f"{self.tutorial.title} - {self.heading}"