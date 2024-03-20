from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm


class PostsListView(generic.ListView):
    model = Post
    template_name = "blog/posts_list.html"
    context_object_name = 'posts'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = 'post'


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_create.html"
    success_url = reverse_lazy('posts_list')


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_update.html"

