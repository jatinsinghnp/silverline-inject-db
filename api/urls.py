from django.urls import path

from .views import Apisent, Apihome,Api_details

urlpatterns = [
    path("", Apisent),
    path("home/",Apihome),
    path("details/<int:id>",Api_details)
]
