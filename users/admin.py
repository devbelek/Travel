from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import GuideApplication


User = get_user_model()


@admin.register(GuideApplication)
class GuideApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'is_approved']
    actions = ['approve_guide']
    readonly_fields = ['name', 'surname', 'resume', 'user']