from django.http import HttpResponse
from rest_framework import generics
from .serializers import TrackDataSerializer
from .models import TrackData


class CreateTrackDataView(generics.ListCreateAPIView):
    """
    this class creates and updates the database using data posted from the frontend.
    """
    queryset = TrackData.objects.all()
    serializer_class = TrackDataSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = TrackData.objects.all()
    serializer_class = TrackDataSerializer


def indexView(req):
    return HttpResponse('this is the index of all the view in that category')

