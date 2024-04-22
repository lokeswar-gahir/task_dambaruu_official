from django.db import models
from authentication.models import User

# Create your models here.

class VideoModel(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content =  models.FileField(upload_to='video/%y')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title