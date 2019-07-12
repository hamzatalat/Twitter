from django.db import models

class SignUpData(models.Model):
    name_text = models.CharField(max_length=200)
    email_text = models.CharField(max_length=200)
    password_text = models.CharField(max_length=200)
