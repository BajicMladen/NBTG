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
    path(
        "password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
    path(
        "password_reset/confirm/",
        include("django_rest_passwordreset.urls", namespace="password_reset_confirm"),
    ),
    path(
        "password_reset/validate_token/",
        include("django_rest_passwordreset.urls", namespace="password_reset_validate"),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
