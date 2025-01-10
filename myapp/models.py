from django.db import models

class Event(models.Model):
    event_title = models.CharField(max_length=255)  # Title of the event
    date = models.DateField()                      # Date of the event
    time = models.CharField(max_length=30)                     # Time of the event
    description = models.TextField()               # Detailed description of the event
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for event creation

    def __str__(self):
        return f"{self.event_title} on {self.date}"

class Prayer_request(models.Model):
    email = models.EmailField(max_length=255)  # To store the user's email address
    request = models.TextField()              # To store the user's prayer request
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the request was created

    def __str__(self):
        return f"Prayer Request from {self.email}"