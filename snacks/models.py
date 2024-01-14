from django.db import models
from django.contrib.auth import get_user_model


#TODO only owners can create instances
class Snack(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['owner', '-created_at']

    def __str__(self):
        return self.name


class Collection(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    snacks = models.ManyToManyField("snacks.Snack", blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

