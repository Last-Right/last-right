from rest_framework import serializers
from .models import Tag, VideoModel


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class VideoModelSerializer(serializers.ModelSerializer):
    # Serializer for the tags field
    tags = TagSerializer(many=True)

    class Meta:
        model = VideoModel
        fields = '__all__'
