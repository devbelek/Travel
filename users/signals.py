from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import GuideApplication, Guides


@receiver(post_save, sender=GuideApplication)
def create_guide(sender, instance, created, **kwargs):
    if instance.is_approved and not created:
        if not Guides.objects.filter(guide=instance).exists():
            Guides.objects.create(guide=instance)
