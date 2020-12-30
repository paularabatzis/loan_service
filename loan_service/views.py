from django.views.generic import ListView
from .models import payment_log, loan
from django.shortcuts import render
from .utils import update_loan_balance

class PaymentList(ListView):
    model = payment_log

def payment_logs(request):
    payments = payment_log.objects.all()
    return render( request, 'loan_service/payment_log.html', {'payments' : payments})

def submit_payment(request):
    payment_amount = request.get('payment_amount')
    loan_name = request.get('loan_name')
    loan = loan.objects.get(loan_name=loan_name)
    update_loan_balance(payment_amount, loan.loan_name, loan.interest_rate)
