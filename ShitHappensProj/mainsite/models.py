from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Story(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    story_content = models.CharField(max_length=2048,null=False)
    create_date = models.DateTimeField(null=False)
    expire_date = models.DateTimeField(null=True)
    like_count = models.IntegerField(null=False)
    dislike_count = models.IntegerField(null=False)
    is_active = models.BooleanField(null=False)
    def __str__(self):
        """
        String for representing the Story object
        """
        return self.story_content[0:20]
    def get_absolute_url(self):
        return reverse('singlestoryurl', args=[str(self.id)])

class Users_LikeStories(models.Model):
    user_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    story_id = models.ForeignKey(Story, null=False, on_delete=models.CASCADE)

class Users_DisLikeStories(models.Model):
    user_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    story_id = models.ForeignKey(Story, null=False, on_delete=models.CASCADE)
    