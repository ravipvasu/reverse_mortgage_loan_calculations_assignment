# Import System Modules
import logging

# Import Third-party Python Modules
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse

# Import Project Modules
from .forms import MortgageForm
from .utils import MortgageCalculator

# Logger variables to be used for logging
info_logger = logging.getLogger('api_info_logger')
error_logger = logging.getLogger('api_db_error_logger')


class MortgageCalculatorView(View):
    form_class = MortgageForm
    template_name = 'calculator/form.html'

    def get(self, request, *args, **kwargs):
        form = None
        try:
            form = self.form_class()
        except Exception as e:
            error_logger.error(e, exc_info=True)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = None
        try:
            form = self.form_class(request.POST)
            if form.is_valid():
                age = form.cleaned_data['age']
                home_value = form.cleaned_data['home_value']
                margin = float(form.cleaned_data['margin'])
                calculator = MortgageCalculator(age, home_value, margin)
                principal_limit = calculator.calculate_principal_limit()
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'principal_limit': str(principal_limit)})
                return render(request, 'calculator/result.html', {'form': form, 'principal_limit': principal_limit})
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'errors': form.errors}, status=400)
        except Exception as e:
            error_logger.error(e, exc_info=True)
        return render(request, self.template_name, {'form': form})
