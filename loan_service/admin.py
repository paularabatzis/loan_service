from django.contrib import admin 
from .models import loan, payment_log

admin.site.register(loan)
admin.site.register(payment_log)
