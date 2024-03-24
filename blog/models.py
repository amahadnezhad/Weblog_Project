from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', _('Published')),
        ('drf', _('Draft')),
    )

    author = models.ForeignKey(get_user_model(), verbose_name=_("Author"), on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_("Title"), max_length=200)
    text = models.TextField(verbose_name=_("Text"),)
    status = models.CharField(choices=STATUS_CHOICES, verbose_name=_("Status"), max_length=3)
    cover = models.ImageField(upload_to='covers/', verbose_name=_("Cover"), blank=True)
    likes = models.ManyToManyField(get_user_model(), verbose_name=_("likes"), related_name='liked_posts', blank=True)
    date_created = models.DateField(auto_now_add=True, verbose_name=_("Date_created"),)
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_("DateTime_Created"),)
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_("DateTime_Modified"),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])


class Like(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name=_("User"), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name=_("Post"), on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_("DateTime_Created"),)

    class Meta:
        unique_together = ("user", "post")


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    is_active = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.text}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.post.id])
