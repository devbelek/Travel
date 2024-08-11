from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Tour, TourLocation, TourDescription, Comment

User = get_user_model()
admin.site.register(TourLocation)


@admin.register(TourDescription)
class TourDescriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'people', 'activityLevel', 'comfortLevel', 'languages', 'journey']


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'images', 'price', 'location', 'guide', 'description']
    list_filter = ['guide']
    search_fields = ['title', 'description']
    fields = ['title', 'images', 'price', 'location', 'guide', 'description']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'tour', 'user', 'text', 'created_at']
    list_filter = ['created_at', 'tour']
    search_fields = ['text', 'user__username', 'tour__title']
    readonly_fields = ['created_at']
