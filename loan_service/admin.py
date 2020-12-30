from django.contrib import admin 
from .models import Loan, payment_log

admin.site.register(Loan)
admin.site.register(payment_log)
