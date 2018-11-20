"""Tests to find compound interest"""

import unittest
from exercise13 import turn_percent_to_decimal, calculate_compounded_interest_rate

class TestCalculateCompoundInterest(unittest.TestCase):
    """Calculate compound interest"""

    def test_decimal_conversion(self):
        """Can I convert a number to a decimal?"""

        interest_rate = 4.5
        generate_decimal = turn_percent_to_decimal(interest_rate)
        self.assertEqual(generate_decimal, 0.045)

    def test_compound_interest_calculation(self):
        """Can I get the compound interest?"""

        principal_amount = 1500
        total_invested_years = 6
        interest_rate = 4.5
        periods_per_year_to_compound = 4
        total_compounded_interest = calculate_compounded_interest_rate(principal_amount, total_invested_years, interest_rate, periods_per_year_to_compound)
        self.assertEqual(total_compounded_interest, 1500.00)

if __name__ == '__main__':
    unittest.main()
