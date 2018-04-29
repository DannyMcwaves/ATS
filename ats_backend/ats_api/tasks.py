from __future__ import absolute_import, unicode_literals
from celery import shared_task
from rest_framework import status
from rest_framework.response import Response
import sys
import os

sys.path.append('..')

from process_pdf import read

__all__ = ['log_data']


@shared_task
def log_data(data):
    # print()
    parsed = read(os.getcwd() + '/' + '/'.join(data['resume'].split('/')[2:]))
    print(parsed)
    return Response(data, status=status.HTTP_201_CREATED)

