from django.conf import settings
from django.db import models

from django.template.defaultfilters import escape
from django.urls import reverse

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Post(models.Model):
    header = models.CharField(max_length=250, verbose_name='заголовок')
    body = models.CharField(max_length=250, verbose_name='текст')
    pic = models.ImageField(upload_to='post_pictures/', **NULLABLE, verbose_name='изображение')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор')
    created = models.DateField(auto_now_add=True, verbose_name='дата создания')
    updated = models.DateField(auto_now=True, verbose_name='дата редактирования')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'Пост {self.header[:15] + "..."} - {self.author} ({self.created})'

    # def user_link(self):
    #     return '<a href="%s">%s</a>' % (reverse("admin:user_change", args=(self.author.pk,)), escape(self.author))
    #
    # user_link.allow_tags = True
    # user_link.short_description = "User"


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор')
    body = models.CharField(max_length=250, verbose_name='текст')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='пост')
    created = models.DateField(auto_now_add=True, verbose_name='дата создания')
    updated = models.DateField(auto_now=True, verbose_name='дата редактирования')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Комментарий {self.author} к {self.post.header[:15] + "..."} ({self.created})'
