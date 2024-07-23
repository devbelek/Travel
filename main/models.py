from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'O нас'
        verbose_name_plural = 'О нас'


class TourLocation(models.Model):
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class Tour(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    location = models.ForeignKey(TourLocation, on_delete=models.CASCADE, blank=False)
    guide = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'