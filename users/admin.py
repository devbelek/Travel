from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from .models import GuideApplication, Tour
from django.core.mail import send_mail

User = get_user_model()


@admin.register(GuideApplication)
class GuideApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'is_approved']
    actions = ['approve_guide']
    readonly_fields = ['name', 'surname', 'resume', 'user']


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'guide']
