import math
from datetime import date
from .models import Loan, PaymentLog

def update_loan_balance(payment_amount, this_loan):
	if (payment_amount != 0):	
		days_since_last_payment = (date.today() - this_loan.last_payment_date).days or 0
		interest = (this_loan.current_amount*this_loan.interest_rate/365)*days_since_last_payment
		this_loan.current_amount = this_loan.current_amount - payment_amount + interest
		this_loan.last_payment_date = date.today()
		this_loan.save()
		log = PaymentLog.objects.create(loan_id=this_loan, payment_date=date.today(), payment_amount=payment_amount, 
		interest_since_last_payment=interest, remaining_balance=this_loan.current_amount)
		log.save()
	return

