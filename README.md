The project using object-oriented programming (OOP) principles in Django:

### Project Structure

1. **Django Setup**
   - A Django project and app.
   - Configured settings and URLs.

2. **Models**
   - No database models needed as the calculation is purely functional.

3. **Views**
   - A class-based view to handle the form and display the results.

4. **Forms**
   - A Django form to collect user inputs: borrower's age and home value.
   - A dropdown for selecting different margins.

5. **Templates**
   - A template to render the form and display results.
   - Used JavaScript with AJAX to update calculations in real-time.

6. **Calculations**
   - A class to handle the principal limit calculation.

7. **Unit Tests**
   - Unit tests to validate the calculation logic.
   - Test views to ensure the form is displayed and calculations are correct.

### Explanation of OOP Implementation

- **Class-Based View**: `MortgageCalculatorView` handles GET and POST requests, rendering forms and results respectively.
- **Calculation Class**: `MortgageCalculator` encapsulates the principal limit calculation logic, making the code modular and reusable.
- **Unit Tests**: Tests create instances of `MortgageCalculator` and verify the correctness of its `calculate_principal_limit` method.

### Running the Application

- Migrate database (though not needed here for any models).
- Run the server:

  ```bash
  python manage.py migrate
  python manage.py runserver
  ```

Navigate to `http://127.0.0.1:8000/` to see the form and use the calculator.
