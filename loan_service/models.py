from django.db import models
from datetime import date

class Loan(models.Model):
	name = models.CharField(max_length = 50)
	start_amount = models.DecimalField(max_digits=20, decimal_places=2)
	current_amount = models.DecimalField(max_digits=20, decimal_places=2)
	last_payment_date = models.DateField(default=date.today())
	interest_rate = models.DecimalField(max_digits=6, decimal_places=4, default=1.0)

	def __str__(self):
		return self.name

class PaymentLog(models.Model):
	loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE)
	payment_date = models.DateField()
	payment_amount = models.DecimalField(max_digits=20, decimal_places=2)
	remaining_balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
	interest_since_last_payment = models.DecimalField(max_digits=20, decimal_places=2)
	
	class meta:
		ordering = ["loan_id", "payment_date", "payment_amount", "interest_since_last_payment"]
