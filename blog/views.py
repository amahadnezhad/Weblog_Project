from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse

from .models import Post, Like
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


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("posts_list")


def like_post(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(id=pk)
        if request.user in post.likes.all():
            # User has already liked the post, so unlike it
            post.likes.remove(request.user)
        else:
            # User has not liked the post, so like it
            post.likes.add(request.user)
        return redirect('post_detail', pk=pk)
    else:
        return redirect('home')
