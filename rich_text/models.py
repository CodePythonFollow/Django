from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Blog(models.Model):
    content = HTMLField()
