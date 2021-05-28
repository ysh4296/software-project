from django.urls import path
from . import views

#app_name = "restaurant"

urlpatterns = [

    path('create/', views.create, name="restaurant_create"),
    path('list/', views.list, name="list"),
    path('detail/', views.detail, name="restaurant-detail"),

    path('restaurant/<int:id>/', views.detail, name="restaurant-detail"),
    path('restaurant/<int:restaurant_id>/review/create/', views.review_create, name='review-create'),
    path('restaurant/<int:restaurant_id>/review/delete/<int:review_id>', views.review_delete, name='review-delete'),

]