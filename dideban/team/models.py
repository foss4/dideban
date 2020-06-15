from django.db import models

from dideban.user.models import User
from utils.common.models import TimestampedModelMixin


class Team(TimestampedModelMixin):
    title = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True, null=True)
