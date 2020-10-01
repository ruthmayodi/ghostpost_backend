from django.db import models
from django.utils import timezone

# Create your models here.
class Posts(models.Model):
    boast = models.BooleanField(default=True)
    text = models.CharField(max_length=200)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    postdate = models.DateTimeField(default=timezone.now)

    @property
    def score(self):
        return self.upvote - self.downvote


