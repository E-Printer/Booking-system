from django.db import models
from django.core.validators import MinValueValidator

class Session(models.Model):
    SESSION_TYPES = [
        ('beginner lesson', 'Beginner Lesson'),
        ('beginner surf', 'Beginner Surf'),
        ('intermediate lesson', 'Intermediate Lesson'),
        ('intermediate surf', 'Intermediate Surf'),
        ('advanced lesson', 'Advanced Surf'),
        ('advanced plus', 'Advanced Plus'),
        ('expert turns', 'Expert Turns'),
        ('expert barrels', 'Expert Barrels'),
    ]

    name = models.CharField(
        max_length=100, 
        blank=True, 
        default='', 
        verbose_name="Session Name", 
        help_text="Name of the session."
    )
    type = models.CharField(
        max_length=100, 
        choices=SESSION_TYPES, 
        verbose_name="Session Type", 
        help_text="Type of surf session."
    )
    description = models.TextField(
        max_length=1000, 
        blank=True, 
        null=True, 
        verbose_name="Session Description", 
        help_text="Detailed description of the session."
    )

    class Meta:
        ordering = ['type', 'name']

    def __str__(self):
        return f"{self.name} ({self.type})"

class SessionInstance(models.Model):
    session = models.ForeignKey(
        Session, 
        on_delete=models.CASCADE, 
        related_name="instances", 
        verbose_name="Session",
        help_text="The session this instance is associated with."
    )
    date = models.DateField(
        verbose_name="Session Date", 
        help_text="Date of the session."
    )
    time = models.TimeField(
        verbose_name="Session Time", 
        help_text="Start time of the session."
    )
    price_per_session = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=60.00, 
        validators=[MinValueValidator(0)],
        verbose_name="Price Per Session", 
        help_text="Price for this session instance."
    )
    max_occupancy = models.IntegerField(
        default=30, 
        validators=[MinValueValidator(1)],
        verbose_name="Maximum Occupancy", 
        help_text="Maximum number of participants for this session instance."
    )

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return f"{self.session.name} on {self.date} at {self.time} - £{self.price_per_session}"
