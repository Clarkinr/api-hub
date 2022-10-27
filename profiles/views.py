from django.db.models import Count
from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from polo_api.permissions import IsOwnerOrReadOnly


"""
Shows List of all previously created profiles
"""


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_time')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_time',
        'owner__followed__created_time',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
