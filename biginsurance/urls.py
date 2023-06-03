from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("success", views.success, name="success"),
    path("oops", views.success, name="oops"),
]