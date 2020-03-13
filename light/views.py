from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, GenericAPIView
from .models import Light
from .serializer import LightModelSerializer

class LightListAPIView(ListAPIView):
    queryset = Light.objects.all()
    serializer_class = LightModelSerializer

class LightCreateAPIView(CreateAPIView):
    queryset = Light.objects.all()
    serializer_class = LightModelSerializer

class LightUpdateAPIView(UpdateAPIView):
    queryset = Light.objects.all()
    serializer_class = LightModelSerializer

class LightOffAPIView(ListAPIView):
    queryset = Light.objects.all()
    serializer_class = LightModelSerializer

    def get(self, request, *args, **kwargs):
        Light.objects.all().update(activate=False)
        return ListAPIView.get(self, request, *args, **kwargs)

class LightOnAPIView(ListAPIView):
    queryset = Light.objects.all()
    serializer_class = LightModelSerializer

    def get(self, request, *args, **kwargs):
        Light.objects.all().update(activate=True)
        return ListAPIView.get(self, request, *args, **kwargs)