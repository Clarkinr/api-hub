from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Club
from django_filters.rest_framework import DjangoFilterBackend
from .serilalizers import ClubSerializer
from polo_api.permissions import IsOwnerOrReadOnly


"""
Shows List of all previously created clubs
"""


class ClubList(generics.ListCreateAPIView):
    queryset = Club.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
    ).order_by('name')
    serializer_class = ClubSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__club',
    ]
    ordering_fields = [
        'followers_count',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ClubDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
