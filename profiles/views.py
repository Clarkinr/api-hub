from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from polo_api.permissions import IsOwnerOrReadOnly


"""
Shows List of all previously created profiles
"""


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
