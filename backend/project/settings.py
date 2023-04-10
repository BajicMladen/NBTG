import os
from datetime import timedelta

import environ

BASE_DIR = environ.Path(__file__) - 2

env = environ.Env()
env.read_env(env_file=BASE_DIR(".env"))


SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", [])

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.shop",
    "apps.user",
    "rest_framework",
    "corsheaders",
    "django_filters",
    "django_rest_passwordreset",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("POSTGRES_DB"),
        "USER": env.str("POSTGRES_USER"),
        "PASSWORD": env.str("POSTGRES_PASSWORD"),
        "HOST": env.str("POSTGRES_HOST"),
        "PORT": env.str("POSTGRES_PORT"),
        "TEST": {"NAME": env.str("POSTGRES_TEST_DB")},
    },
}


MEDIA_URL = "/media/"
MEDIA_ROOT = str(BASE_DIR("media"))

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "user.User"
STATIC_ROOT = env.str("STATIC_ROOT", None) or BASE_DIR / "staticfiles"
ENVIRONMENT = env.str("ENVIRONMENT")

# DRF
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
        "rest_framework.permissions.DjangoModelPermissions",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    # "DEFAULT_PAGINATION_CLASS": ["rest_framework.pagination.PageNumberPagination"],
    # "PAGE_SIZE": 2,
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

# PASSWORD RESET
DJANGO_REST_PASSWORDRESET_TOKEN_CONFIG = {
    "CLASS": "django_rest_passwordreset.tokens.RandomStringTokenGenerator",
    "OPTIONS": {"min_length": 20, "max_length": 30},
}

# DJANGO_REST_MULTITOKENAUTH_RESET_TOKEN_EXPIRY_TIME = 1
DJANGO_REST_PASSWORDRESET_NO_INFORMATION_LEAKAGE = True

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD")

CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", [])

if DEBUG:
    REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"].append(
        "rest_framework.authentication.SessionAuthentication"
    )
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"].append(
        "rest_framework.renderers.BrowsableAPIRenderer"
    )


# Logging
DJANGO_LOG_PATH = env.str("DJANGO_LOG_PATH")
DJANGO_LOG_LEVEL = env.str("DJANGO_LOG_LEVEL")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "{levelname} {message}", "style": "{"},
        "verbose": {
            "format": "\n\t".join(
                [
                    "[{levelname}] {name} {asctime}",
                    'Module: "{module}"',
                    'Module path: "{pathname}"',
                    'Line number: "{lineno}"',
                    'Message: "{message}"',
                ]
            )
            + "\n",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": DJANGO_LOG_LEVEL,
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file": {
            "level": DJANGO_LOG_LEVEL,
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(DJANGO_LOG_PATH, f"django-{ENVIRONMENT}.log"),
            "backupCount": 10,  # Keep 10 files max
            "maxBytes": 5242880,  # 5 MB
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "level": DJANGO_LOG_LEVEL,
            "propagate": False,
        },
    },
}
