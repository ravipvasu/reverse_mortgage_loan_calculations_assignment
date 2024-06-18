from django import forms
from decimal import Decimal

MARGINS = [(Decimal(i), f"{i}%") for i in range(1, 11)]


class MortgageForm(forms.Form):
    age = forms.IntegerField(label='Age', min_value=62, max_value=100)
    home_value = forms.FloatField(label='Home Value')
    margin = forms.ChoiceField(label='Margin', choices=MARGINS)
