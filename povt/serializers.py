from rest_framework import serializers
from povt.models import Order

class TextListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class TextDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'