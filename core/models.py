from django.db import models
from django.utils.text import slugify


class SkillCategory(models.TextChoices):
    TECHNICAL = "technical", "Technical"
    RESEARCH = "research", "Research"
    SOFT = "soft", "Soft Skills"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.CharField(max_length=20, choices=SkillCategory.choices)
    icon = models.CharField(max_length=50, blank=True, help_text="Icon class or emoji")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Timeline(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_education = models.BooleanField(default=False)
    is_ongoing = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-start_date", "-order"]

    def __str__(self):
        return f"{self.title} at {self.organization}"

    @property
    def date_range(self):
        if self.is_ongoing or not self.end_date:
            return f"{self.start_date.strftime('%b %Y')} - Present"
        return (
            f"{self.start_date.strftime('%b %Y')} - {self.end_date.strftime('%b %Y')}"
        )


class Profile(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    short_bio = models.TextField(max_length=500, help_text="Short bio for hero section")
    bio = models.TextField(help_text="Full bio for about page")
    profile_image = models.ImageField(upload_to="profile/", blank=True, null=True)
    cv = models.FileField(upload_to="cv/", blank=True, null=True)
    email = models.EmailField()
    location = models.CharField(max_length=200, blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    google_scholar = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    skills = models.ManyToManyField(Skill, blank=True, related_name="profiles")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name

    def get_skills_by_category(self):
        return {
            "technical": self.skills.filter(category=SkillCategory.TECHNICAL),
            "research": self.skills.filter(category=SkillCategory.RESEARCH),
            "soft": self.skills.filter(category=SkillCategory.SOFT),
        }
