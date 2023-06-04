from rest_framework import serializers
from .models import Client as Clienting

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clienting
        fields = "__all__"