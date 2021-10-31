from django.db import models
from django.contrib.auth.models import User

# News
class News(models.Model):
    title = models.CharField(max_length=50)
    link = models
    creation_date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)
    author_name = models.ForeignKey(User, related_name='UserPosts', on_delete=models.CASCADE)

    def count_votes(self):
        return self.votes.all().count()

    def __str__(self):
        return self.title


# Votes
class Votes(models.Model):
    user = models.ForeignKey(User, related_name="UserVotes", on_delete=models.CASCADE)
    news = models.ForeignKey(News, related_name="NewsVotes", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'news')

# Comments
class Comments(models.Model):
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    content = models.TextField('comment text')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.content

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии' 
        ordering = ('-creation_date',)