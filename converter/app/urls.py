from django.urls import path
from . import views
urlpatterns = [
    path("", views.landingpage, name="landingpage"),
    path("login", views.login_view, name="loginpage"),
    path("qcm", views.qcm, name="qcmpage"),
]