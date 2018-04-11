
from rest_framework import serializers
from .models import TrackData

__all__ = ['TrackDataSerializer']


class TrackDataSerializer(serializers.ModelSerializer):
    """
    serializer to map model instance into json formats
    """

    class Meta:
        """
        meta class to map serializer fields into model fields
        """
        model = TrackData
        fields = ('description', 'resume', 'id', 'created', 'modified')
        read_only_fields = ('created', 'modified', 'id')
