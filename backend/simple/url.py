from django.urls import path
from . import views

urlpatterns =[
    path('', views.Routes, name ='routes'),
    path('products/', views.getPrds, name ='products'),
    path('products/<str:product_id>/', views.getPrd, name ='product'),
    path('products/sizes/<str:product_id>/', views.getCps)
]