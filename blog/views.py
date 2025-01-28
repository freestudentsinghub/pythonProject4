from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from blog.models import Blog


# ListView
class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog.html"

    def get_queryset(self):
        return Blog.objects.filter(published=True)


# DetailView
class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_views += 1
        self.object.save()
        return self.object


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

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])

# DeleteView
class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog')


