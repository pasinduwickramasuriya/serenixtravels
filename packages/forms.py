from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['guest_name', 'guest_email', 'guest_phone', 'travel_date', 'number_of_guests', 'message']
        widgets = {
            'guest_name': forms.TextInput(attrs={
                'class': 'w-full px-6 py-4 bg-slate-50 border border-slate-200 rounded-2xl focus:ring-2 focus:ring-indigo-600 focus:border-transparent outline-none transition-all',
                'placeholder': 'Full Name'
            }),
            'guest_email': forms.EmailInput(attrs={
                'class': 'w-full px-6 py-4 bg-slate-50 border border-slate-200 rounded-2xl focus:ring-2 focus:ring-indigo-600 focus:border-transparent outline-none transition-all',
                'placeholder': 'Email Address'
            }),
            'guest_phone': forms.TextInput(attrs={
                'class': 'w-full px-6 py-4 bg-slate-50 border border-slate-200 rounded-2xl focus:ring-2 focus:ring-indigo-600 focus:border-transparent outline-none transition-all',
                'placeholder': 'Phone Number'
            }),
            'travel_date': forms.DateInput(attrs={
                'class': 'w-full px-6 py-4 bg-slate-50 border border-slate-200 rounded-2xl focus:ring-2 focus:ring-indigo-600 focus:border-transparent outline-none transition-all',
                'type': 'date'
            }),
            'number_of_guests': forms.NumberInput(attrs={
                'class': 'w-full px-6 py-4 bg-slate-50 border border-slate-200 rounded-2xl focus:ring-2 focus:ring-indigo-600 focus:border-transparent outline-none transition-all',
                'placeholder': 'Number of Guests'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full px-6 py-4 bg-slate-50 border border-slate-200 rounded-2xl focus:ring-2 focus:ring-indigo-600 focus:border-transparent outline-none transition-all',
                'placeholder': 'Special Requests or Questions',
                'rows': 4
            }),
        }
