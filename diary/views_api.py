from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter

from django_filters import rest_framework as filters
from django_filters import FilterSet

from .models import Record, Writer
from .serializers import RecordSerializer


class RecordFilter(FilterSet):
    date = filters.DateFromToRangeFilter()
    writer = filters.ModelChoiceFilter(queryset=Writer.objects.all())

    class Meta:
        model = Record
        fields = ['writer', 'date']


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filterset_class = RecordFilter
    ordering_fields = ['date']

    def get_queryset(self):
        return Record.objects.filter(writer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)
