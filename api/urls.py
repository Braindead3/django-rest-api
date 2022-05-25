from django.contrib import admin
from django.urls import path, include
from .views import CategoryCreateView,ClothListCreateView,ClothUpdateView

urlpatterns = [
    path('cloth/', ClothListCreateView.as_view()),
    path('cloth/<int:pk>/', ClothUpdateView.as_view()),
    path('category/', CategoryCreateView.as_view()),
]
