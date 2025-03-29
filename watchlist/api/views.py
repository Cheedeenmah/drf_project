from rest_framework import generics
from watchlist.models import StreamPlatform,WatchList,Review
from .serializers import StreamPlatformSerializer, WatchListSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class StreamPlatformView(generics.ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StreamPlatformDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


class WatchListView(generics.ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return WatchList.objects.filter(platform=pk)

class WatchListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= WatchList.objects.all()
    serializer_class = WatchListSerializer

class ReviewView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    