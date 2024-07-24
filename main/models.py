from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class TourLocation(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.FileField(upload_to='LocationImages/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class Tour(models.Model):
    title = models.CharField(max_length=255)
    images = models.FileField(upload_to='tours_images/')
    included = models.CharField(max_length=200)
    not_included = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey(TourLocation, on_delete=models.CASCADE)
    guide = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.OneToOneField('TourDescription', on_delete=models.CASCADE, null=True, blank=True)
    itinerary = models.OneToOneField('TourItinerary', on_delete=models.CASCADE, null=True, blank=True)
    place_to_live = models.OneToOneField('PlaceToLive', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


class Comment(models.Model):
    tour = models.ForeignKey(Tour, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.tour.title}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class TourDescription(models.Model):
    LANGUAGES_CHOICES = (
        ('english', 'English'),
        ('russian', 'Russian'),
    )
    people = models.PositiveIntegerField()
    activityLevel = models.CharField(max_length=20)
    comfortLevel = models.CharField(max_length=20)
    languages = models.CharField(max_length=20, choices=LANGUAGES_CHOICES)
    journey = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.people} people, {self.activityLevel} activity"

    class Meta:
        verbose_name = 'Тур описание'
        verbose_name_plural = 'Описание туров'


class TourItinerary(models.Model):
    place = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    images = models.FileField(upload_to='itinerary_images/')

    def __str__(self):
        return self.place

    class Meta:
        verbose_name = 'Тур Маршрут'
        verbose_name_plural = 'Маршруты туров'

class PlaceToLive(models.Model):
    description = models.CharField(max_length=350)
    images = models.FileField(upload_to='place_to_live_images/')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'