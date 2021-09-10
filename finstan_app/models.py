from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.forms.fields import FilePathField

# Create your models here.
class FileStat(models.Model):
    file_path = models,FilePathField(upload_to = 'statements')
    user = models.ForeignKey(User, on_delete=CASCADE, required = False, null=True)

