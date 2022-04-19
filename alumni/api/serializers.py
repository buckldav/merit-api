from rest_framework import serializers
from alumni.models import Alum


class AlumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alum
        fields = '__all__'
