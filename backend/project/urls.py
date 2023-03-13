from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from apps.user.views import UserViewset

v1_api = routers.DefaultRouter()
v1_api.trailing_slash = r"/?"

v1_api.register("user", UserViewset, "user")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(v1_api.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
