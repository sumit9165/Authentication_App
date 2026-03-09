from django.urls import path
from customer.views import CustomerDashboardView, CustomerPasswordChangeView


urlpatterns = [
    path('dashboard', CustomerDashboardView.as_view(), name='customer_dashboard'),
    path('password-change/', CustomerPasswordChangeView.as_view(), name='password_change'),
]
