from django.db import models

# Create your models here.
# this connects to the database
# model for the to do list
# model for the to do 

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"Title: {self.title}"