from django.db import models
from django.db import User


class Tour(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    guide = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class GuideApplication(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    surname = models.CharField(max_length=35)
    resume = models.FileField(upload_to='resumes/', blank=False)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.surname}"