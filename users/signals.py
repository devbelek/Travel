from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import CustomUser, GuideRegistration
from allauth.account.models import EmailAddress
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


@receiver(post_save, sender=CustomUser)
def create_guide_registration(sender, instance, created, **kwargs):
    if created and instance.is_guide:
        GuideRegistration.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_guide_registration(sender, instance, **kwargs):
    if hasattr(instance, 'guide_registration'):
        instance.guide_registration.save()


class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        email = sociallogin.account.extra_data.get('email', '').lower()
        if email:
            try:
                email_address = EmailAddress.objects.get(email__iexact=email)
                if email_address.user:
                    sociallogin.connect(request, email_address.user)
            except EmailAddress.DoesNotExist:
                pass
