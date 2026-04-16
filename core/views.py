from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Profile, Timeline, Skill
from blog.models import BlogPost
from projects.models import Project


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.filter(is_active=True).first()
        context["featured_projects"] = Project.objects.filter(featured=True)[:3]
        context["latest_posts"] = BlogPost.objects.filter(published=True)[:3]
        return context


class AboutView(TemplateView):
    template_name = "core/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.filter(is_active=True).first()
        context["timeline"] = Timeline.objects.all()
        context["skills"] = Skill.objects.all()
        return context
