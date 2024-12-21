from django.shortcuts import render, redirect
from .models import Slot, Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required

@login_required
def view_slots(request):
    slots = Slot.objects.filter(is_available=True)
    return render(request, 'bookings/view_slots.html', {'slots': slots})

@login_required
def book_slot(request, slot_id):
    slot = Slot.objects.get(id=slot_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.slot = slot
            booking.save()
            slot.is_available = False
            slot.save()
            return redirect('view_bookings')
    else:
        form = BookingForm()
    return render(request, 'bookings/book_slot.html', {'form': form, 'slot': slot})

@login_required
def view_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/view_bookings.html', {'bookings': bookings})
