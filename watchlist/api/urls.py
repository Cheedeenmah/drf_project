from django.urls import path
from .views import StreamPlatformView,StreamPlatformDetail,WatchListView,WatchListDetail,ReviewView,ReviewDetail

urlpatterns = [
    path('platform/', StreamPlatformView.as_view()),
    path('platform/<int:pk>/', StreamPlatformDetail.as_view()),
    path('movie/<int:pk>/platform/', WatchListView.as_view()),
    path('movie/<int:pk>/', WatchListDetail.as_view()),
    path('reviews/', ReviewView.as_view()),
    path('reviews/<int:pk>/', ReviewDetail.as_view()),
    ]