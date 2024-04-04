from .views import *
from django.urls import path

urlpatterns = [
    path("page/",page, name="page"),
]