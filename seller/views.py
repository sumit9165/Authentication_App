from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import IsSellerMixin
# Create your views here.
class SellerDashboardView(LoginRequiredMixin, View, IsSellerMixin):
    def get(self, request, *args, **kwargs):
        return render(request, 'seller/dashboard.html')