from django.db import models
from dideban.user.models import User
from django.utils import timezone

class Team(models.Model):
    title = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now)
