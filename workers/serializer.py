from rest_framework import serializers
from .models import Shift, Mounth, Worker

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['name', 'surname']

class ShiftSerializer(serializers.ModelSerializer):
    worker = WorkerSerializer()
    class Meta:
        model = Shift
        fields = ['worker', 'date']
