from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Tour, About, TourLocation, Booking

User = get_user_model()

admin.site.unregister(User)

@admin.register(TourLocation)
class TourLocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'location']
    search_fields = ['location']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
    search_fields = ['title']


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'location', 'guide']
    list_filter = ['location', 'guide']
    search_fields = ['title', 'description']
    fields = ['title', 'description', 'price', 'location', 'guide']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'tour', 'phone_num', 'booking_date', 'status']
    list_filter = ['status', 'booking_date']
    search_fields = ['user__username', 'tour__title']
    date_hierarchy = 'booking_date'
    ordering = ['-booking_date']
    fields = ['user', 'tour', 'phone_num', 'status']
    readonly_fields = ['phone_num', 'tour', 'user']
