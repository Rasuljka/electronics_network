from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import NetworkNode
from .permissions import IsActiveUser
from .serializers import NetworkNodeSerializer


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['contact_info__country']
    ordering_fields = ['created_at', 'name']
    permission_classes = [IsActiveUser]
