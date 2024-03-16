from django.shortcuts import render
from django.views import generic

from .models import Post


class PostsListView(generic.ListView):
    model = Post
    template_name = "blog/posts_list.html"
    context_object_name = 'posts'
