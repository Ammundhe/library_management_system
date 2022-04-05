from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="HomePage")
]
