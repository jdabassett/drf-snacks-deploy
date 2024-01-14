from rest_framework import serializers

from .models import Snack, Collection


class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "owner", "name", "description", "created_at", "updated_at"]
        model = Snack


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "owner", "snacks"]
        model = Collection
