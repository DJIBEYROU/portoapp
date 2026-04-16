from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    color = models.CharField(
        max_length=20, default="#0EA5E9", help_text="Hex color code"
    )

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=350, unique=True)
    content = models.TextField()
    excerpt = models.TextField(
        max_length=500, blank=True, help_text="Short summary for cards"
    )
    featured_image = models.ImageField(upload_to="blog/", blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.published and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    @property
    def reading_time(self):
        words = len(self.content.split())
        minutes = max(1, round(words / 200))
        return f"{minutes} min read"
