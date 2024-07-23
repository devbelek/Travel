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

    def approve_guide(self, request, queryset):
        for application in queryset:
            if not application.is_approved:
                application.is_approved = True
                application.save()

                password = get_random_string(length=8)

                user = User.objects.create_user(
                    username=application.user.username,
                    email=application.user.email,
                    password=password
                )

                send_mail(
                    'Ваш аккаунт гида одобрен',
                    f'Ваш логин: {application.user.username}\nВаш пароль: {password}',
                    'from@example.com',
                    [application.user.email],
                    fail_silently=False,
                )
        self.message_user(request, "Выбранные гиды были одобрены и уведомлены.")

    approve_guide.short_description = "Одобрить выбранных гидов"

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'guide']
