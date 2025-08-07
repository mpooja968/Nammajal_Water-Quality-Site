# frontend/models.py

from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    reset_token = models.CharField(max_length=255, blank=True, null=True)  # Add this line

    def __str__(self):
        return self.email
    
class Lake(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Complaint(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    issue = models.CharField(max_length=200)
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.issue}"
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    comments = models.TextField()
    rating = models.PositiveIntegerField()  # Use PositiveIntegerField for ratings 1 to 5

    def __str__(self):
        return self.name
    

    
