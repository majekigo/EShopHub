from django.urls import path
from user import views

urlpatterns = [
    path('userprofile/', views.userprofile, name='userprofile'),
    path('cart/', views.cart, name='cart'),
    path('feedback/', views.feedback, name='feedback')
]