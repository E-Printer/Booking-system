from django.shortcuts import render, redirect, get_object_or_404
from .models import Slot, Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib import messages




def view_slots(request):
    surf_sessions = [
        {"type": "Beginner Lesson"},
        {"type": "Beginner Session"},
        {"type": "Waikiki Lesson"},
        {"type": "Waikiki Session"},
        {"type": "Intermediate Lesson"},
        {"type": "Intermediate Session"},
        {"type": "Advanced Lesson"},
        {"type": "Advanced Session"},
        {"type": "Advanced Plus Session"},
        {"type": "Expert Turns Session"},
        {"type": "Expert Barrels Session"},
    ]
    return render(request, 'view_slots.html', {"surf_sessions": surf_sessions})


@login_required
def book_slot(request, session_type):
    """
    Create an instance of a booking and send a confirmation email.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            try:
                slot = Slot.objects.get(session_type=session_type, date=date, time=time, is_available=True)
                booking = form.save(commit=False)
                booking.user = request.user
                booking.slot = slot
                booking.save()
                slot.is_available = False
                slot.save()
                messages.success(request, "Slot booked successfully!")
                return redirect('view_bookings')
            except Slot.DoesNotExist:
                messages.error(request, "No Slot matches the given query.")
        else:
            messages.error(request, "Invalid form submission.")
    else:
        form = BookingForm()

    available_slots = Slot.objects.filter(session_type=session_type, is_available=True)
    
    return render(request, 'book_slot.html', {
        'form': form,
        'session_type': session_type,
        'available_slots': available_slots,
    })


@login_required
def view_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'view_bookings.html', {'bookings': bookings})


class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = "base.html"  