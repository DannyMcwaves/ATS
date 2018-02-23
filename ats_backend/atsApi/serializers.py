
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
        fields = ('id', 'username', 'job_description', 'resume', 'resume_words', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
