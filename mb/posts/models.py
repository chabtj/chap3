from django.db import models

# Create your models here.
class Message(models.Model):

	message=models.TextField(max_length=100)

	def __str__(self):
		return self.message[:50]