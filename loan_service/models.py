from django.db import models
from datetime import date

class loan(models.Model):
	name = models.CharField(max_length = 50)
	start_amount = models.DecimalField(max_digits=20, decimal_places=2)
	current_amount = models.DecimalField(max_digits=20, decimal_places=2)
	last_payment_date = models.DateField(default=date.today())
	interest_rate = Models.DecimalField(max_digits=2, decimal_places=4)

	def __str__(self):
		return self.name

class payment_log(models.Model):
	loan_id = models.ForeignKey(loan, on_delete=models.CASCADE)
	payment_date = models.DateField()
	payment_amount = models.DecimalField(max_digits=20, decimal_places=2)
	interest_since_last_payment = models.DecimalField(max_digits=20, decimal_places=2)
	
	class meta:
		ordering = ["loan_id", "payment_date", "payment_amount", "interest_since_last_payment"]

	def __str__(self):
		return self.loan_id
