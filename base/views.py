from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Car
from .Serializer import CarSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthenticatedReadOnly

# Create your views here.

@api_view()
def index(request):
    return Response("hello")

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes=[IsAuthenticatedReadOnly]