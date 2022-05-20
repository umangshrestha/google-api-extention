from rest_framework import fields, serializers
from .models import *


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ('id', 'name', 'project_id', 'private_key_id')

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = '__all__'


class OnlyUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = '__all__'
        
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'



