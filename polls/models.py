from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    icon = models.ImageField(upload_to='static/media/post_icon/')
    userId = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    checked = models.BooleanField(blank=False, null=False, default=False)
    createDate = models.DateField(auto_now_add=True, auto_now=False)
    modifiedDate = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s (%s)" % (self.id, self.title)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Candidate(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=64, blank=False, null=False)
    description = models.TextField(max_length=300, blank=True, null=True, default='')
    voteCount = models.IntegerField(blank=False, null=False, default=0)
    photo = models.ImageField(upload_to='static/media/candidate_photo/')

    def __str__(self):
        return "Candidate %s %s" % (self.id, self.name)

    def get_id(self):
        return self.id

    class Meta:
        verbose_name = 'Candidate'
        verbose_name_plural = 'Candidates'


class User_Candidate(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    candidateId = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True, blank=True)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "%s - %s" % (self.userId, self.candidateId)

    class Meta:
        unique_together = (('userId', 'candidateId'),)
