from django.contrib.auth.mixins import UserPassesTestMixin
from django.http.response import HttpResponseForbidden
from django.shortcuts import redirect

erro_403_html = """


{% load static %}
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="">
        <style>
            /* General Styles */
            body{
            margin:0;
            font-family: Arial, sans-serif;
            background-color: #f3f4f6;
            display: flex;
            height:100vh;
            }

            .container{
                background-color:#ffffff;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                border-radius:8px;
                text-align: center;
                max-width: 400px;
                width: 100px;
            }
            h1 {
                font-size:32px;
                color:#e3342f;
                margin-bottom: 20px;
            }
            p {
                font-size:16px;
                color: 4a4a4a;
                margin-bottom: 20px;
            }
            a {
                background-color: #3490dc;
                font-weight: bold;
                color:#ffffff;
                padding: 12px 24px;
                display: inline-block;
                text-decoration: none;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                transition: background-color 0.3s, box-shadow 0.3s;
            }
            a:hover {
                background-color: #2779bd;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
    </head>
    <body>
        <div class="container>
            <h1>403 - Access Forbidden</h1>
            <p> Sorry, you are not authorized to access this page.</p>
            <a href="" >Return to Home</a>
        </div>
    </body>
</html>

"""


class IsCustomerMixin(UserPassesTestMixin):

    def test_func(self):
        # type: ignore
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, "is_customer")
            and self.request.user.is_customer
        )

    def handle_no_permission(self):  # type: ignore
        if self.request.user.is_authenticated:  # type: ignore
            return HttpResponseForbidden(erro_403_html)
        return redirect("login")


class IsSellerMixin(UserPassesTestMixin):

    def test_func(self):
        # type: ignore
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, "is_seller")
            and self.request.user.is_seller
        )

    def handle_no_permission(self):  # type: ignore
        if self.request.user.is_authenticated:  # type: ignore
            return HttpResponseForbidden(erro_403_html)
        return redirect("login")
