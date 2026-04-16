from django.db import models
from django.utils.text import slugify


class ProjectTag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    color = models.CharField(max_length=20, default="#0EA5E9")

    class Meta:
        verbose_name = "Project Tag"
        verbose_name_plural = "Project Tags"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    gallery = models.JSONField(
        default=list, blank=True, help_text="List of additional image URLs"
    )
    technologies = models.ManyToManyField(
        ProjectTag, blank=True, related_name="projects"
    )
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["-featured", "-order", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def tech_list(self):
        return list(self.technologies.all())
