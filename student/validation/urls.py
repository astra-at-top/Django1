from django.urls import path
from .views import Auths, Login

urlpatterns = [
    path("login", Login.as_view(), name="login"),
    path("signup", Auths.as_view(), name="signup"),
]
