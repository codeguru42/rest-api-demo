# Create your views here.
from rest_framework import viewsets

from rest import models, serializers


class BaseballCardViewSet(viewsets.ModelViewSet):
    queryset = models.BaseballCard.objects.all()
    serializer_class = serializers.BaseballCardSerializer
