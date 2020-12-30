from django.views.generic import ListView
from .models import PaymentLog, Loan
from django.shortcuts import render
from .utils import update_loan_balance

class PaymentList(ListView):
    model = PaymentLog

def payment_logs(request):
    payments = PaymentLog.objects.all()
    return render( request, 'loan_service/payment_log.html', {'payments' : payments})

def submit_payment(request):
    payment_amount = request.POST.get('payment_amount', 0)
    loan_name = request.POST.get('loan_name', 'pauls car loan')
    loan = Loan.objects.get(name=loan_name)
    update_loan_balance(payment_amount, loan)
    payments = PaymentLog.objects.filter(loan_id=loan)
    return render( request, 'loan_service/payment_log.html', {'payments' : payments})
