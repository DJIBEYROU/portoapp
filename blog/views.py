from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import BlogPost, Tag


class BlogListView(ListView):
    model = BlogPost
    template_name = "blog/blog_list.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        queryset = BlogPost.objects.filter(published=True)

        tag = self.request.GET.get("tag")
        if tag:
            queryset = queryset.filter(tags__slug=tag)

        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["selected_tag"] = self.request.GET.get("tag")
        return context


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog/blog_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return BlogPost.objects.filter(published=True)

    def get_object(self, **kwargs):
        obj = super().get_object(**kwargs)
        obj.views += 1
        obj.save(update_fields=["views"])
        return obj
