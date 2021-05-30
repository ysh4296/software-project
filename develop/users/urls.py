from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("edit/", views.EditView.as_view(), name="edit"),
    path(("logout/"), views.log_out, name="logout"),
]
