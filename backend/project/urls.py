from apps.user.views import SignInViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from project.api import api
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("sign-in/", SignInViewSet.as_view()),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
