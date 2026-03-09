from django.urls import path
from seller.views import SellerDashboardView


urlpatterns = [
    path('dashboard/', SellerDashboardView.as_view(), name='seller_dashboard'),
]
