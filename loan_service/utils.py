import math
from datetime import date
from .models import Loan, PaymentLog

def update_loan_balance(payment_amount, this_loan):
	days_since_last_payment = (this_loan.last_payment_date - date.today()).days or 0
	interest = 0
	for i in range(days_since_last_payment):
		interest += interest*(interest_rate/365)
	this_loan.current_amount = this_loan.current_amount - payment_amount + interest
	this_loan.last_payment_date = date.today()
	this_loan.save()
	log = PaymentLog.objects.create(loan_id=this_loan, payment_date=date.today(), payment_amount=payment_amount, 
		interest_since_last_payment=interest)
	log.save()
	return

