from django.urls import path
from account import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='Login'),
    path('logout',views.Logout, name='Logout'),
    path('create-account', views.create_account.as_view(), name="Create_account"),
]