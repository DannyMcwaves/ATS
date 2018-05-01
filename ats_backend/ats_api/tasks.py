from __future__ import absolute_import, unicode_literals
from celery import shared_task
# from rest_framework import status
# from rest_framework.response import Response
import sys
import os

sys.path.append('..')

from process_pdf import read

__all__ = ['process_info']


@shared_task
def log(data):
    print(data)


@shared_task
def read_pdf(data):
    log(data)
    return read(os.getcwd() + '/' + '/'.join(data.split('/')[2:]))


@shared_task
def read_job_description(data):
    return data.split(' ')


def process_info(data):
    pdf = read_pdf(data['resume'])
    return {
        'resume_data': [word for page in pdf for word in page],
        'job_data': read_job_description(data['description'])
    }
