class MortgageCalculator:
    def __init__(self, age, home_value, margin):
        self.age = age
        self.home_value = home_value
        self.margin = margin

    def calculate_principal_limit(self):
        principal_limit = self.home_value * (self.age / 100) * (1 - self.margin / 100)
        return round(principal_limit, 2)

    # def calculate_principal_limit(self):
    #     factor = (self.age - 62) / 100
    #     principal_limit = self.home_value * factor * (1 - self.margin / 100)
    #     return round(principal_limit, 2)

    # def calculate_principal_limit(self):
    #     """
    #     Principal Limit = min(IPL,MCA)
    #     Maximum Claim Amount (MCA) in 2022 is $970,800 (https://goodlifehomeloans.com/glossary/maximum-claim-amount/)
    #
    #     IPL = Appraised Value (home_value) x LTV Ratio
    #     LTV Ratio = LTV Factor−Age Factor−Margin Factor
    #
    #     LTV Ratio = LTV Factor−(Age Factor×age)−(Margin Factor×margin)
    #     Where:
    #
    #     LTV Factor is a constant based on program guidelines.
    #     Age Factor adjusts the LTV ratio based on the borrower's age.
    #     Margin Factor adjusts the LTV ratio based on the selected margin (interest rate).
    #     LTV Factor:
    #     The Loan-to-Value (LTV) Factor is a constant that represents the maximum percentage of the home's appraised value that can be borrowed. It's often influenced by the borrower's age and prevailing interest rates.
    #     For example, a typical LTV Factor might be around 0.5 to 0.6, meaning 50% to 60% of the home's value can be borrowed.
    #
    #     Age Factor:
    #     The Age Factor adjusts the LTV ratio based on the borrower's age. As the borrower's age increases, the LTV ratio tends to decrease.
    #     It's often expressed as a percentage or a multiplier that decreases the LTV ratio linearly as the borrower gets older.
    #     For example, an Age Factor of 0.01 means the LTV ratio decreases by 1% for every year increase in age.
    #
    #     Margin Factor:
    #     The Margin Factor represents the adjustable interest rate added to a predetermined index rate (such as LIBOR or the Treasury index) to determine the interest rate on the reverse mortgage.
    #     It's typically expressed as a decimal or percentage and directly affects the LTV ratio. Higher margins result in lower LTV ratios and vice versa.
    #     For example, a Margin Factor of 0.02 represents an additional 2% added to the index rate.
    #     """
    #     import random
    #     mca = 970800
    #     ipl = 0
    #     ltv_factor = random.uniform(0.5, 0.6)
    #     age_factor = 0.01
    #     margin_factor = 0.02  # hypothetical value
    #     ltv_ratio = ltv_factor - (age_factor * self.age) - (margin_factor * self.margin)
    #     ipl = self.home_value * ltv_ratio
    #     principal_limit = min(ipl, mca)
    #     return round(principal_limit, 2)
