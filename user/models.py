from django.db import models
from signup.models import SignUpData


class User(models.Model):	
	u_name = models.ForeignKey(SignUpData, on_delete=models.CASCADE)
	
class Tweets(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	tweet = models.CharField(max_length=200)
	likes = models.IntegerField(default=0)

class comments (models.Model):
	tweet = models.ForeignKey(Tweets, on_delete=models.CASCADE)
	text = 	models.CharField(max_length=200 ,default='')
	likes = models.IntegerField(default=0)
