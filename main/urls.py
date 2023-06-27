from django.urls import path
from . import views

app_name = 'last-right'

urlpatterns = [
    path('', views.BadRequestView.as_view(), name='bad_request'),
    path('api/videos', views.VideoList.as_view(), name='video-list'),
    # path('api/videos/<int:video_id>', views.VideoDetail.as_view(), name='video-detail'),
    # path('api/videos/<int:video_id>/comments', views.VideoComments.as_view(), name='video-comments'),
    # path('api/search', views.VideoSearch.as_view(), name='video-search'),
]
