from .views import *
from django.urls import path
from Admin_dashboard import admin as custom_admin


urlpatterns = [
    path("",index, name="index"),
    path('admin/', custom_admin.admin_site.urls),
]
