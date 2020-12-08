from django.db import models

# THIS REPRESENTS A TABLE IN OUR DB
class User(models.Model): # inherits from models.Model
  #id is imlpicit
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  age = models.PositiveSmallIntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
