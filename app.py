from __future__ import absolute_import

from celery import Celery
from celery.utils.log import get_task_logger as logger


__all__ = ['app', 'logger']

app = Celery('ats')

app.config_from_object('celeryconfig')
