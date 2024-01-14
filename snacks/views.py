from rest_framework import generics

from .models import Snack, Collection
from snacks.serializers import SnackSerializer, CollectionSerializer
from snacks_project.permissions import IsOwnerOrReadOnly



class SnackListCreate(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = SnackSerializer
    queryset = Snack.objects.all()


class SnackUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = SnackSerializer
    queryset = Snack.objects.all()


class CollectionListCreate(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = CollectionSerializer
    queryset = Snack.objects.all()


class CollectionUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = CollectionSerializer
    queryset = Snack.objects.all()

