from .models import Status  # Model
from .serializers import StatusSerializer  # Serializer based on Status Model

from rest_framework import parsers, viewsets

# Create your views here.


class StatusViewset(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
