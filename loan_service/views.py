from django.views.generic import ListView
from .models import PaymentLog, Loan
from django.shortcuts import render
from .utils import update_loan_balance
from decimal import Decimal

class PaymentList(ListView):
    model = PaymentLog

def payment_logs(request):
    loan_id = request.GET.get('loan_name', 1)
    loan = Loan.objects.get(id=loan_id)
    loans = Loan.objects.all()
    payments = PaymentLog.objects.filter(loan_id=loan)
    return render( request, 'loan_service/paymentlog_list.html', {'payments' : payments, 'loans' : loans})

def submit_payment(request):
    payment_amount = request.POST.get('payment_amount', 0)
    decimal_payment_amount = Decimal(payment_amount)
    loan_id = request.POST.get('loan_name', 1)
    loan = Loan.objects.get(id=loan_id)
    loans = Loan.objects.all()
    update_loan_balance(decimal_payment_amount, loan)
    return render( request, 'loan_service/submit_payment.html', {'loans' : loans})
