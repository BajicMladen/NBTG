import logging
import os

from django.conf import settings

from celery import Celery, signals

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

app = Celery(getattr(settings, "CELERY_TASK_NAME_PREFIX"))
app.config_from_object(settings, namespace="CELERY")
app.autodiscover_tasks()


@signals.setup_logging.connect
def on_celery_setup_logging(**kwargs):
    config = getattr(settings, "LOGGING")

    celery_log_path = getattr(settings, "CELERY_LOG_PATH")
    celery_log_level = getattr(settings, "CELERY_LOG_LEVEL")
    environment = getattr(settings, "ENVIRONMENT")

    config["loggers"] = {
        "celery": {
            "handlers": ["console", "file"],
            "level": celery_log_level,
            "propagate": False,
        }
    }
    config["handlers"]["file"]["level"] = celery_log_level
    config["handlers"]["file"]["filename"] = os.path.join(celery_log_path, f"celery-{environment}.log")

    logging.config.dictConfig(config)
