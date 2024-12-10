# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm  # Import your custom registration form
from django.contrib import messages
from django.contrib.auth.views import LoginView

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)  # Use your custom form here
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created!')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()  # Create an empty form instance

    return render(request, 'registration/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


