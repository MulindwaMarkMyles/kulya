from .views import *
from django.urls import path


urlpatterns = [
    path("page/",page, name="page"),
    path("admin_page/",admin_page,name="admin_page"),
    path("business_list/",business_list,name="business_list"),
    path("business_create/",business_create,name="business_create"),
    path("business_delete/<int:pk>/",business_delete,name="business_delete"),
    path("business_detail/",business_detail,name="business_detail"),
]
