from django.db import models
from django.utils.text import slugify


class Service(models.Model):
    CATEGORY_CHOICES = [
        ("Engineering", "Engineering"),
        ("Consulting", "Consulting"),
        ("Manufacturing", "Manufacturing"),
        ("Support", "Support"),
        ("Other", "Other"),
    ]

    title = models.CharField(max_length=300)
    short_title = models.CharField(max_length=150, blank=True)
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    description = models.TextField()
    hero_subtitle = models.CharField(max_length=500)
    content = models.TextField()
    cta = models.CharField(max_length=200)
    cta_secondary = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="services/", blank=True, null=True)

    # Intro section fields
    intro_heading = models.CharField(max_length=300, blank=True)
    intro_subheading = models.TextField(blank=True)
    intro_content = models.TextField(blank=True)

    # What We Provide heading
    what_we_provide_heading = models.CharField(max_length=300, blank=True)

    # Problems We Solve heading
    problems_we_solve_heading = models.CharField(max_length=300, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ServiceProvideItem(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="provide_items"
    )
    text = models.CharField(max_length=500)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.text[:100]


class ServiceProblem(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="problem_items"
    )
    title = models.CharField(max_length=300)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class ServiceStat(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="stats"
    )
    value = models.CharField(max_length=50)
    label = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.label}: {self.value}"


class ServiceStep(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="steps"
    )
    step = models.PositiveIntegerField()
    title = models.CharField(max_length=300)
    description = models.TextField()
    icon = models.TextField(help_text="SVG path data for the icon")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"Step {self.step}: {self.title}"


class ServiceCapability(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="capabilities"
    )
    text = models.CharField(max_length=500)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.text[:100]