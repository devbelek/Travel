from .models import GuideApplication, Guides
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

@receiver(post_save, sender=GuideApplication)
def create_guide(sender, instance, created, **kwargs):
    if instance.is_approved and not created:
        if not Guides.objects.filter(guide=instance).exists():
            Guides.objects.create(guide=instance)
