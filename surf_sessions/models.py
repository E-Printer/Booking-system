from django.db import models
from django.contrib.auth.models import User
from datetime import date
from datetime import date, time as dt_time

class Slot(models.Model):
    date = models.DateField()
    time = models.TimeField()
    session_type = models.CharField(max_length=100, default='Beginner')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.session_type} - {self.date} - {self.time}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(default=date.today)
    time = models.TimeField(default=dt_time(9, 0))

    def __str__(self):
        return f"Booking by {self.user} on {self.date} at {self.time}"
