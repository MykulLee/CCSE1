from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth import get_user_model
from django.apps import apps


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)  # Hashing
        user.save(using=self._db)
        return user


    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractUser):
    security_answer = models.CharField(max_length=255, null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'volleyball_customuser'


class Volleyball(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Volleyball, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Volleyball, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

    
    
