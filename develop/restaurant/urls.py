from django.urls import path
from . import views
from django.views.generic import TemplateView

#app_name = "restaurant"

urlpatterns = [

    path('create/', views.create, name="restaurant_create"),
    path('list/', views.list, name="list"),
    path('detail/', views.detail_model.as_view(), name="restaurant-detail"),

    path('restaurant/<int:id>/', views.detail_model.as_view(), name="restaurant-detail"),
    path('restaurant/<int:restaurant_id>/review/create/', views.Review_model.as_view(), name='review-create'),
    path('restaurant/<int:restaurant_id>/review/delete/<int:review_id>', views.review_delete, name='review-delete'),

]