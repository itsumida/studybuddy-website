from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    courses = models.ManyToManyField('Course', related_name='students')
    availability = models.CharField(max_length=255, help_text="e.g., Weekdays 6-8 PM")
    study_methods = models.CharField(max_length=255, help_text="e.g., Group study, Flashcards")
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.email


class Course(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True) 
    description = models.TextField()

    def __str__(self):
        return f"{self.code} - {self.name}"
    
class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name  

class StudyMatch(models.Model):
    user1 = models.ForeignKey(User, related_name='matches_initiated', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='matches_received', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user1.username} & {self.user2.username} - {self.status}"
    
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='messages_sent', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='messages_received', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username} at {self.timestamp}"

class Review(models.Model):
    reviewer = models.ForeignKey(User, related_name='given_reviews', on_delete=models.CASCADE)
    reviewed_user = models.ForeignKey(User, related_name='received_reviews', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=5)  # Rating out of 5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.reviewed_user.username} by {self.reviewer.username} - {self.rating}⭐"







