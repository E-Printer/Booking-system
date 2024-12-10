from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from .forms import BookingForm

# Create your views here

# List all active services
def service_list(request):
    services = Service.objects.filter(is_active=True)
    return render(request, 'services/service_list.html', {'services': services})

# Book a specific service
def book_service(request, service_id):
    service = get_object_or_404(Service, id=service_id, is_active=True)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.service = service
            booking.user = request.user  # Assuming users are logged in
            booking.save()
            return redirect('booking_success')  # Redirect to a success page
    else:
        form = BookingForm()
    return render(request, 'services/book_service.html', {'service': service, 'form': form})

