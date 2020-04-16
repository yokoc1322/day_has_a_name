from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Record
from .serializers import RecordSerializer


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['date']
    ordering_fields = ['date']

    def get_queryset(self):
        return Record.objects.filter(writer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)
