from rest_framework.serializers import ModelSerializer
from .models import Light

class LightModelSerializer(ModelSerializer):
    class Meta:
        model = Light
        fields = '__all__'