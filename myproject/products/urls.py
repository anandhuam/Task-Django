from django.urls import path
from . import views

urlpatterns = [
    # Product URLs
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/create/', views.product_create, name='product_create'),
    path('product/<int:pk>/edit/', views.product_update, name='product_update'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),

    # ProductVariant URLs
    path('variants/', views.product_variant_list, name='product_variant_list'),
    path('variant/<int:pk>/', views.product_variant_detail, name='product_variant_detail'),
    path('variant/create/', views.product_variant_create, name='product_variant_create'),
    path('variant/<int:pk>/edit/', views.product_variant_update, name='product_variant_update'),
    path('variant/<int:pk>/delete/', views.product_variant_delete, name='product_variant_delete'),
]
