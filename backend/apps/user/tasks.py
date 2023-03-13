import logging

from celery.schedules import crontab
from project.celery import app as celery_app

logger = logging.getLogger("celery")


@celery_app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10, say_hello.s("World"), name="Say hello to the World every 10 seconds")
    sender.add_periodic_task(
        crontab(hour=16, minute=1),
        say_hello.s("World"),
        name="Say hello to the World every day at 16:01",
    )


@celery_app.task
def say_hello(person: str):
    logger.info(f"Hello {person}")
