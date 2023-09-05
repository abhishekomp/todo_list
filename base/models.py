from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  title = models.CharField(max_length=200) # null by default is False. Title cannot be null
  description = models.TextField(null=True, blank=True)
  complete = models.BooleanField(default=False)
  createdDateTime = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
  
  class Meta:
    ordering = ['complete'] # This means that when all objects are fetched all complete items will be down in the list

