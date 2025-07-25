from django.urls import path
from .views import homepage, SignUp, Login, logout_view

app_name = "home"
urlpatterns = [
    path("", homepage, name="homepage"),
    path("sign_up/", SignUp.as_view(), name="sign_up"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
]
