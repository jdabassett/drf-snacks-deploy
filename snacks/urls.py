from django.urls import path
from .views import SnackListCreate, SnackUpdateDelete, CollectionListCreate, CollectionUpdateDelete


urlpatterns = [
    path("snacks/", SnackListCreate.as_view(), name="snack_list_create" ),
    path("snacks/<int:pk>", SnackUpdateDelete.as_view(), name="snack_update_delete"),
    path("collection/", CollectionListCreate.as_view(), name="collection_list_create"),
    path("collection/<int:pk>", CollectionUpdateDelete.as_view(), name="collection_update_delete"),
]