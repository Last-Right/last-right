from django.contrib import admin
from .models import VideoModel, Tag


admin.site.register(Tag)
admin.site.register(VideoModel)
