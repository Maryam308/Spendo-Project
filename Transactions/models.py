from django.db import models

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('Deposit', 'Deposit'),
        ('Withdraw', 'Withdraw'),
    ]

    CATEGORY_CHOICES = [
    ('Shopping', 'Shopping'),
    ('Car Inspection', 'Car Inspection'),
    ('Travel Saving', 'Travel Saving'),
    ('Groceries', 'Groceries'),
    ('Utilities', 'Utilities'),
    ('Rent', 'Rent'),
    ('Entertainment', 'Entertainment'),
    ('Dining Out', 'Dining Out'),
    ('Health & Fitness', 'Health & Fitness'),
    ('Education', 'Education'),
    ('Clothing', 'Clothing'),
    ('Gifts', 'Gifts'),
    ('Home Improvement', 'Home Improvement'),
    ('Transportation', 'Transportation'),
    ('Subscription Services', 'Subscription Services'),
    ('Miscellaneous', 'Miscellaneous'),
    ('Other', 'Other'),
    ]


    transaction_date = models.DateField()
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    transaction_category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.transaction_type} - {self.transaction_amount} on {self.transaction_date}"
