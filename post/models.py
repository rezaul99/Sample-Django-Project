from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()

    class Meta:
        verbose_name_plural = 'Blog post'

    @classmethod
    def number_of_recentposts(cls):
        return True

    def __str__(self):
        return self.title
