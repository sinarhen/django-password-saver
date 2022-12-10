from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Password(models.Model):
    password = models.CharField(max_length=55)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='saved_password', editable=False)

    def __str__(self):
        return f'PASSW {self.pk}'
