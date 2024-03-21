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
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    if user.is_authenticated:
        if Like.objects.filter(user=user, post=post).exists():
            # If the user has already liked the post, unlike it
            Like.objects.filter(user=user, post=post).delete()
            post.likes_count -= 1
            post.save()
        else:
            # If the user hasn't liked the post yet, like it
            Like.objects.create(user=user, post=post)
            post.likes_count += 1
            post.save()
    else:
        return redirect(reverse('account_login'))

    return redirect(reverse('post_detail', kwargs={'pk': pk}))
