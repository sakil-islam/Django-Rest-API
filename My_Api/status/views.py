from .models import Status  # Model
from .serializers import StatusSerializer  # Serializer based on Status Model

from rest_framework import generics, parsers

# Create your views here.


class StatusListCreateView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]


class StatusDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
