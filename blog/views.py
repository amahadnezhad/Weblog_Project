from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext as _

from .models import Post, Comment
from .forms import PostForm, CommentForm


class PostsListView(generic.ListView):
    template_name = "blog/posts_list.html"
    paginate_by = 4
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_created')


@login_required
def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
            messages.success(request, _("Comment Added SuccessFully"))
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', context={'post': post, 'comments': comments,
                                                             'comment_form': comment_form, })


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_create.html"
    success_url = reverse_lazy('posts_list')


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_update.html"


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("posts_list")


@login_required
def like_post(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(id=pk)
        if request.user in post.likes.all():
            # User has already liked the post, so unlike it
            post.likes.remove(request.user)
            messages.error(request, _("Post Has Unliked"))
        else:
            # User has not liked the post, so like it
            post.likes.add(request.user)
            messages.success(request, _("Post Has Liked"))

        return redirect('post_detail', pk=pk)
    else:
        return redirect('home')

