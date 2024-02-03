from django import forms
from django.core.validators import MinValueValidator

from .models import Garment, Payment


class GarmentSchedulePaymentForm(forms.ModelForm):
    class Meta:
        model = Garment
        fields = ['name', 'description', 'type', 'quantity']

    quantity = forms.IntegerField(validators=[MinValueValidator(0)])
    date = forms.DateField()
    time = forms.TimeField()
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    status = forms.ChoiceField(choices=Payment.STATUS_CHOICES, initial='Pending')
    mode_of_payment = forms.ChoiceField(choices=Payment.MODE_CHOICES, initial='CreditCard')
