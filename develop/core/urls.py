from django.urls import path
from . import views
from users import views as user_views

app_name = "core"

urlpatterns = [
    path("", user_views.home, name="home"),
]
