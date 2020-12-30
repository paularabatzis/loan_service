from django.contrib import admin 
from .models import Loan, PaymentLog

admin.site.register(Loan)
admin.site.register(PaymentLog)
