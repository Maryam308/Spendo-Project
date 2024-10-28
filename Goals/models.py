from django.db import models
from django.utils import timezone

class Goal(models.Model):
    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Expired', 'Expired'),
    ]

    title = models.CharField(max_length=100)  # Goal title
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Goal amount
    added_on = models.DateField(auto_now_add=True)  # Automatically set to current date when created
    due_date = models.DateField()  # Due date
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Started')  # Status

    def __str__(self):
        return f"{self.title} - {self.amount} (Due: {self.due_date})"

    def check_status(self):
        """Updates the status of the goal based on the due date."""
        if self.status != 'Completed' and timezone.now().date() > self.due_date:
            self.status = 'Expired'
            self.save()  # Save the updated status to the database


new_goal = Goal(
    title='Save for New Laptop',  # Set the goal title
    amount=1200.00,                # Set the goal amount
    due_date='2025-01-01'          # Set the due date
)