from django.db import models
from users.models import User


class Friend(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    birthday_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
