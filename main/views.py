from .models import VideoModel
from .serializers import VideoModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class VideoList(APIView):
    def get(self, request):
        # Retrieves the list of tags from the 'tags' query parameter
        tags = request.GET.getlist('tags')

        # Logic to retrieve a list of videos
        # videos = YourVideoModel.objects.all()
        videos = VideoModel.objects.filter(tags__name__in=tags)

        # Serialize the videos data if needed
        serializer = VideoModelSerializer(videos, many=True)
        serialized_data = serializer.data

        # Return the serialized data as a response
        return Response(serialized_data)
