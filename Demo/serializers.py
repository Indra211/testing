from rest_framework import serializers
from .models import Details,Slots


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slots
        fields = '__all__'
