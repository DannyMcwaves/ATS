from rest_framework import generics
from .serializers import TrackDataSerializer
from .models import TrackData
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .tasks import log_data


class CreateTrackDataView(generics.ListCreateAPIView):
    """
    this class creates and updates the database using data posted from the frontend.
    """
    queryset = TrackData.objects.all()
    serializer_class = TrackDataSerializer

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = TrackDataSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return log_data(file_serializer.data)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = TrackData.objects.all()
    serializer_class = TrackDataSerializer


@api_view(['GET'])
def indexView(req, fmt=None):
    return Response({'data': reverse('api:trackdata', request=req, format=fmt)})

