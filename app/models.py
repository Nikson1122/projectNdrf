from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    is_app_admin = models.BooleanField(default=False)

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    pdf = models.FileField(upload_to='event_pdfs/', blank=True, null=True)

    def __str__(self):
        return self.title
