from django import forms
from .models import Booking, Slot

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ("date", "time")
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Fetch all available times
        available_times = Slot.objects.filter(is_available=True).distinct('time')
        self.fields['time'].choices = [(slot.time, slot.time) for slot in available_times]
