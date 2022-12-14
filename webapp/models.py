from django.conf import settings
from django.db import models
from django.utils import timezone

class Article(models.Model):
    article_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article_title = models.CharField(max_length=500)
    article_text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.article_title

# Create your models here.
