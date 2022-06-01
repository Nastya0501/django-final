from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser, User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    reader_id = models.CharField(max_length=15, null=True, blank=True)
    iin = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return f'Profile: {self.user.username} {self.reader_id}'
