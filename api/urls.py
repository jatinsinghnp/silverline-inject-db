from django.urls import path

from .views import Apisent, Apihome

urlpatterns = [
    path("", Apisent),
    path("get/",Apihome)
]
