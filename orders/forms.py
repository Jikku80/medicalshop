from django import forms
from .models import Order
from django.utils.translation import gettext_lazy as _


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name',
                  'email', 'address', 'ward_no', 'city', 'pay_via']

        labels = {
            'first_name': _('first name'),
            'last_name': _('last name'),
            'email': _('e-mail'),
            'address': _('address'),
            'ward_no': _('ward no'),
            'city': _('city'),
            'pay_via': _('Pay Via')
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control bg-dark text-white'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control bg-dark text-white'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-dark text-white'}),
            'address': forms.TextInput(attrs={'class': 'form-control bg-dark text-white'}),
            'ward_no': forms.NumberInput(attrs={'class': 'form-control bg-dark text-white'}),
            'city': forms.TextInput(attrs={'class': 'form-control bg-dark text-white'}),
            'pay_via': forms.Select(attrs={'class': 'form-control bg-dark text-white', 'id': 'selector'})
        }
