from django.urls import path
from .views import MortgageCalculatorView

urlpatterns = [
    path('', MortgageCalculatorView.as_view(), name='calculate'),
]
