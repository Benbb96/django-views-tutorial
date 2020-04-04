from django.db import models
from datetime import datetime


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(null=False)
    website = models.URLField()
    created_at = models.DateTimeField(default=datetime.now())
    last_seen = models.DateTimeField()
