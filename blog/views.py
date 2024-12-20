from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, TemplateView, DeleteView

from blog.models import Blog


# ListView
class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog.html"


# DetailView
class BlogDetailView(DetailView):
    model = Blog


# CreateView
class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'published', 'number_views',)
    success_url = reverse_lazy('blog:blog')


# UpdateView
class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'published', 'number_views',)
    success_url = reverse_lazy('blog:blog')


# DeleteView
class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog')


