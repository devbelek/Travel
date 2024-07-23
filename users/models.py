from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

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