from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural =  'Categories'


class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    priority = models.IntegerField(default=3)
    is_finished = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
