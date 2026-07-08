from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from core.mixins import IsCustomerMixin


# Create your views here.
class CustomerDashboardView(LoginRequiredMixin, View, IsCustomerMixin):
    def get(self, request, *args, **kwargs):
        return render(request, "customer/dashboard.html")


# type: ignore
class CustomerPasswordChangeView(PasswordChangeView, LoginRequiredMixin, IsCustomerMixin):
    template_name = "customer/password_change.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        logout(self.request)
        messages.success(
            self.request,
            "Password changed successfully. Please log in with your new password.",
        )
        return response

    def form_invalid(self, form):
        messages.error(
            self.request,
            "There was an error changing your password. Please try again",
        )
        return super().form_invalid(form)
