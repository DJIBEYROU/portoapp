from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Project, ProjectTag


class ProjectListView(ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = "projects"

    def get_queryset(self):
        queryset = Project.objects.all()

        tag = self.request.GET.get("tag")
        if tag:
            queryset = queryset.filter(technologies__slug=tag)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = ProjectTag.objects.all()
        context["selected_tag"] = self.request.GET.get("tag")
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"
    context_object_name = "project"
