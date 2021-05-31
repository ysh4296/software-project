from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.all_products_by_category, name='all_products'),
    path(
        '<str:category_slug>/',
        views.all_products_by_category,
        name='all_products_by_category'
    ),
    path(
        '<str:category_slug>/<str:product_slug>/',
        views.product_detail,
        name='product_detail'
    )
]
