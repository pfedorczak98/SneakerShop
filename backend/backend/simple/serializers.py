from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product
from .models import Copies
class ProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CopySerializer(serializers.ModelSerializer):
    #_id = ProdSerializer(many=True)
    class Meta:
        model = Copies
        fields = '__all__'
