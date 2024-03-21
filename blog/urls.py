from django.urls import path

from .views import PostsListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, like_post

urlpatterns = [
    path('', PostsListView.as_view(), name='posts_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('post/new', PostCreateView.as_view(), name="post_create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/like/', like_post, name='like_post'),

]
