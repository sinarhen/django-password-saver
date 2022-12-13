from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.core.exceptions import ValidationError


def validate_notempty(value):
    if len(value) == '0':
        raise ValidationError('Should not be empty')


class Password(models.Model):
    password = models.CharField(max_length=55, validators=[validate_notempty])
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='saved_password', editable=False)

    def __str__(self):
        return f'PASSW {self.pk}'
