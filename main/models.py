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


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name='Тур')
    num_people = models.PositiveIntegerField(verbose_name='Количество людей')
    booking_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата бронирования')
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'В ожидании'), ('Confirmed', 'Подтверждено'), ('Cancelled', 'Отменено')],
        default='Pending',
        verbose_name='Статус'
    )

    def __str__(self):
        return f'{self.user.username} - {self.tour.title}'

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'