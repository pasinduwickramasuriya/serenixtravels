from django.contrib import admin
from .models import HeroSlider, TourPackage, Booking

@admin.register(HeroSlider)
class HeroSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title')

@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration', 'is_featured')
    list_filter = ('is_featured',)
    search_fields = ('name', 'description')
    fieldsets = (
        (None, {'fields': ('name', 'price', 'duration', 'image', 'is_featured')}),
        ('Details', {'fields': ('description', 'itinerary', 'inclusions', 'exclusions')}),
    )

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('package', 'guest_name', 'guest_email', 'guest_phone', 'travel_date', 'created_at','message',)
    list_filter = ('package', 'travel_date')
    search_fields = ('guest_name', 'guest_email', 'package__name')
    readonly_fields = ('created_at',)
