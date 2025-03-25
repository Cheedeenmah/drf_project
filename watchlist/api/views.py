from rest_framework import generics
from watchlist.models import StreamPlatform,WatchList,Review
from .serializers import StreamPlatformSerializer, WatchListSerializer, ReviewSerializer

class StreamPlatformView(generics.ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

class StreamPlatformDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


class WatchListView(generics.ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

class WatchListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= WatchList.objects.all()
    serializer_class = WatchListSerializer

class ReviewView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    