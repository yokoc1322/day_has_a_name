from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import Writer, Record


class RecordSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')

    class Meta:
        model = Record
        fields = ['writer', 'title', 'content', 'date', 'status']


class LoginSerializesr(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
