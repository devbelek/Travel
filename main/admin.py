from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Tour
from django.contrib.auth.models import User, Group


User = get_user_model()

admin.site.unregister(User)
admin.site.unregister(Group)



@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'guide']
