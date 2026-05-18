from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import TourPackage, Booking
from .forms import BookingForm

def package_list(request):
    packages = TourPackage.objects.all()
    return render(request, 'packages/list.html', {'packages': packages})

def package_detail(request, pk):
    package = get_object_or_404(TourPackage, pk=pk)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.package = package
            booking.save()
            
            # Send Emails
            subject = f"New Booking Request: {package.name}"
            message = f"""
            New booking request for {package.name}
            
            Guest Details:
            Name: {booking.guest_name}
            Email: {booking.guest_email}
            Phone: {booking.guest_phone}
            Travel Date: {booking.travel_date}
            Guests: {booking.number_of_guests}
            
            Message:
            {booking.message}
            """
            
            # Email to Admin
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL if hasattr(settings, 'ADMIN_EMAIL') else 'hello@serenix.travel'],
                fail_silently=True,
            )
            
            # Email to Guest
            guest_subject = f"Your Booking Request for {package.name} - Serenix Travels"
            guest_message = f"""
            Hi {booking.guest_name},
            
            Thank you for your interest in our {package.name} tour. We have received your booking request and our team will get back to you shortly.
            
            Booking Summary:
            Package: {package.name}
            Date: {booking.travel_date}
            Guests: {booking.number_of_guests}
            
            Best regards,
            The Serenix Travels Team
            """
            send_mail(
                guest_subject,
                guest_message,
                settings.DEFAULT_FROM_EMAIL,
                [booking.guest_email],
                fail_silently=True,
            )
            
            messages.success(request, 'Your booking request has been sent successfully!')
            return redirect('package_detail', pk=pk)
    else:
        form = BookingForm()
        
    return render(request, 'packages/detail.html', {
        'package': package,
        'form': form
    })
