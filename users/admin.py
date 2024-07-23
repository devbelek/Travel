from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import GuideApplication, Guides

User = get_user_model()


@admin.register(Guides)
class GuidesAdmin(admin.ModelAdmin):
    list_display = ('guide',)
    search_fields = ('guide__name', 'guide__surname')
    readonly_fields = ['guide']


@admin.register(GuideApplication)
class GuideApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'is_approved']
    list_filter = ('is_approved',)
    search_fields = ('name', 'surname')
    actions = ['approve_guide']
    readonly_fields = ['name', 'surname', 'resume', 'user']