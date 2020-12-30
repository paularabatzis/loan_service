from django.views.generic import ListView
from .models import payment_log
from django.shortcuts import render

class PaymentList(ListView):
    model = payment_log

def payment_logs(request):
    payments = payment_log.objects.all()
    return render( request, 'loan_service/payment_log.html', {'payments' : payments})