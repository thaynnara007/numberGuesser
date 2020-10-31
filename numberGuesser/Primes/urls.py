from django.urls import path

from .views import PrimesView


app_name = "primes"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('primes/', PrimesView.as_view()),
]
