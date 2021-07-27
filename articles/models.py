from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

    @property
    def number_of_comments(self):
        return Comment.objects.filter(article=self).count()

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=60)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')

    class Meta:
        ordering = ['-date']