from django.urls import path
from . import views

urlpatterns = [
    path('submit/buy/', views.submit_buy),
    path('',views.home)
]
