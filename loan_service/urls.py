"""loan_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from loan_service.views import PaymentList
from loan_service import views
app_name = 'loan_service'

urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),
    url(r'payment_log', PaymentList.as_view()),
    url(r'payment_log_html', views.payment_logs),
    url(r'make_payment', views.submit_payment)
]
