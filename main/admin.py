from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Tour, TourLocation, TourDescription, TourItinerary, PlaceToLive, Comment

User = get_user_model()
admin.site.unregister(User)

@admin.register(TourDescription)
class TourDescriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'people', 'activityLevel', 'comfortLevel', 'languages', 'journey']

@admin.register(TourItinerary)
class TourItineraryAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'images']

@admin.register(PlaceToLive)
class PlaceToLiveAdmin(admin.ModelAdmin):
    pass

@admin.register(TourLocation)
class TourLocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'title', 'content', 'image']
    search_fields = ['name']

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'images', 'included', 'not_included', 'price', 'location', 'guide', 'description', 'itinerary', 'place_to_live']
    list_filter = ['location', 'guide']
    search_fields = ['title', 'description']
    fields = ['title', 'images', 'included', 'not_included', 'price', 'location', 'guide', 'description', 'itinerary', 'place_to_live']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'tour', 'user', 'text', 'created_at']
    list_filter = ['created_at', 'tour']
    search_fields = ['text', 'user__username', 'tour__title']
    readonly_fields = ['created_at']
