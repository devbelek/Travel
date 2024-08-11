from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices, null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.user.username

class GuideApplication(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    surname = models.CharField(max_length=35)
    resume = models.FileField(upload_to='resumes/', blank=False)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = 'Список заявок на роль Гида'
        verbose_name_plural = 'Список заявок на роль Гида'


class Guides(models.Model):
    guide = models.OneToOneField(GuideApplication, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Список гидов'
        verbose_name_plural = 'Список гидов'
