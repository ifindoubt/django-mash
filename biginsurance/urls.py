from django.urls import path

from .views import ClientSpecs, ClientDetail

urlpatterns = [
    path("", ClientSpecs.as_view()),
    path("<str:pk>", ClientDetail.as_view())
]