from django.db import models
# Create your models here.


class UserEmail(models.Model):
	email = models.EmailField()


