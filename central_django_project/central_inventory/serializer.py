from rest_framework import serializers
from .models import *

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = '__all__'
        
class iapSerializer(serializers.ModelSerializer):
    class Meta:
        model = iap
        fields = '__all__'

class switchSerializer(serializers.ModelSerializer):
    class Meta:
        model = switch
        fields = '__all__'

