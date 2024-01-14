from django.contrib import admin
from .models import Snack, Collection


class SnackAdmin(admin.ModelAdmin):
    list_display = ("owner","name","created_at")


class CollectionAdmin(admin.ModelAdmin):
    list_display = ("owner",)


admin.site.register(Snack, SnackAdmin)
admin.site.register(Collection, CollectionAdmin)

