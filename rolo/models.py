from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=255, null=True)
    contact = models.IntegerField()
    email = models.EmailField(max_length=255, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.user


class Garment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name


class Schedule(models.Model):
    garment = models.OneToOneField(Garment, on_delete=models.CASCADE, related_name='schedule')
    date = models.DateField()
    time = models.TimeField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.garment


class Payment(models.Model):
    garment = models.OneToOneField(Garment, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    payment_date = models.DateTimeField(auto_now_add=True, null=True)

    STATUS_CHOICES = [
        ('Unpaid', 'Unpaid'),
        ('Paid', 'Paid'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    MODE_CHOICES = [
        ('CreditCard', 'Credit Card'),
        ('DebitCard', 'Debit Card'),
        ('BankTransfer', 'Bank Transfer'),
        ('Cash', 'Cash'),
        # Add more choices as needed
    ]
    mode_of_payment = models.CharField(max_length=20, choices=MODE_CHOICES, default='CreditCard')

    def __str__(self):
        return self.amount
