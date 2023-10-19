from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import ShiftSerializer
from .models import Shift

class ShiftView(ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
