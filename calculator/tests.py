from django.test import TestCase
from .utils import MortgageCalculator


class PrincipalLimitCalculationTests(TestCase):
    def test_calculate_principal_limit(self):
        calculator = MortgageCalculator(62, 500000, 3)
        self.assertAlmostEqual(calculator.calculate_principal_limit(), 300700.0)
        calculator = MortgageCalculator(70, 300000, 2)
        self.assertAlmostEqual(calculator.calculate_principal_limit(), 205800.0)
        calculator = MortgageCalculator(80, 250000, 1)
        self.assertAlmostEqual(calculator.calculate_principal_limit(), 198000.0)
