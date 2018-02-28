from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import TrackData

# Create your tests here.


class ModelTestCase(TestCase):
    """
    this is the class that defines the model test case for the applicant tracking data.
    """

    def setUp(self):
        """
        setting the track data
        :return:
        """
        self.username = 'Danny Mcwaves'
        self.job_description = 'hardworking, articulate, efficient, react, es6, python, javascript, redux'
        self.resume = '../pdf_samples/eddie_jung.pdf'
        self.resume_words = 'hardworking,communicative,redux,es6,javascript,efficacious,' \
                            'django,flask,api,experience'
        self.trackData = TrackData(username=self.username, job_description=self.job_description,
                                   resume=self.resume, resume_words=self.resume_words)

    def test_model_can_create_tracking_data(self):
        """
        try to save the model to see if it can save tracking data.
        :return:
        """
        old_count = TrackData.objects.count()
        self.trackData.save()
        new_count = TrackData.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """
    this is the class that defines the view test case for the api
    """

    def setUp(self):
        """
        setting requests for the views.
        :return:
        """
        self.client = APIClient()
        self.track_data = {
            'username': 'Danny Mcwaves',
            'resume': '../pdf_samples/eddie_jung',
            'resume_words': 'hardworking,communicative,redux,es6,javascript,efficacious,django,flask,api,experience',
            'job_description': 'hardworking,articulate,efficient,redux,es6,javascript'
        }
        self.response = self.client.post(reverse('api:trackdata'), self.track_data, format='json')

    def test_api_can_upload_trackdata(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_trackdata(self):
        trackdata = TrackData.objects.get(id=1)
        response = self.client.get(reverse('api:details', kwargs={'pk': trackdata.id}), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertContains(response, trackdata)
