from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    service_id = models.CharField(max_length=100, null=False)
    text = models.TextField(null=False)

    def __str__(self):
        return 'comment' + str(self.user) + str(self.service_id)

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=False)
    text = models.TextField(null=False)

    def __str__(self):
        return 'reply' + str(self.user) + str(self.comment)
